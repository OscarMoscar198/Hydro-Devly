from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from pymongo import DESCENDING
from pdf_generator import generar_pdf
from calculator import statistical_calculator
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder="Public", static_url_path="/Public")
app.config['MONGO_URI'] = 'mongodb+srv://sensorsDevly:devly1@sensorsdevly.wnv4cc4.mongodb.net/Sensors'
app.config['SECRET_KEY'] = 'b99878292951aa53e17598417a4a0a0121fcd0808ef8ae13f76a786a09bdaa4f'
mongo = PyMongo(app)

CORS(app)

@app.route("/login", methods=["POST"])
@cross_origin(origin="http://localhost:3000", headers=["Content-Type"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    # Buscar al usuario en la base de datos MongoDB
    user = mongo.db.users.find_one({"username": username})

    if user and check_password_hash(user["password"], password):
        # Generar el token JWT
        token = jwt.encode(
            {"username": username}, app.config["SECRET_KEY"], algorithm="HS256"
        )
        return jsonify({"token": token})

    return jsonify({"message": "Credenciales inválidas"}), 401


@app.route("/register", methods=["POST", "OPTIONS"])
@cross_origin(origin="http://localhost:3000", headers=["Content-Type"])
def register():
    email = request.json.get("email")
    username = request.json.get("username")
    password = request.json.get("password")

    # Verificar si el email ya existe en la base de datos
    existing_email = mongo.db.users.find_one({"email": email})
    if existing_email:
        return jsonify({"message": "El email ya está en uso"}), 400

    # Verificar si el usuario ya existe en la base de datos
    existing_user = mongo.db.users.find_one({"username": username})
    if existing_user:
        return jsonify({"message": "El nombre de usuario ya está en uso"}), 400

    # Generar un hash de la contraseña
    password_hash = generate_password_hash(password)

    # Crear un nuevo usuario en la base de datos
    new_user = {"email": email, "username": username, "password": password_hash}
    mongo.db.users.insert_one(new_user)

    return jsonify({"message": "Usuario registrado exitosamente"}), 201


@app.route('/api/calcular', methods=['GET'])
def obtener_documentos():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'message': 'Token faltante'}), 401

    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = payload['username']
        documentos = mongo.db.Datos.find().sort("_id", DESCENDING).limit(50)
        campoTemperature_output = []
        campoHumidity_output = []
        campoWaterTem_output = []
        campoLight_output = []
        campoPH_output = []
        campoConduc_output = []
        for documento in documentos:
            campoTemperature_output.append(documento['temperature'])
            campoHumidity_output.append(documento['humidity'])
            campoWaterTem_output.append(documento['waterTem'])
            campoLight_output.append(documento['light'])
            campoPH_output.append(documento['pH'])
            campoConduc_output.append(documento['conduc'])
        pdf_filename = 'ReporteSensores.pdf'
        # Realizar la operación
        arr_sorted_campoTemperature = campoTemperature_output[:50] if len(campoTemperature_output) >= 50 else campoTemperature_output
        arr_sorted_campoHumidity = campoHumidity_output[:50] if len(campoHumidity_output) >= 50 else campoHumidity_output
        arr_sorted_campoWaterTem = campoWaterTem_output[:50] if len(campoWaterTem_output) >= 50 else campoWaterTem_output
        arr_sorted_campoLight = campoLight_output[:50] if len(campoLight_output) >= 50 else campoLight_output
        arr_sorted_campoPH = campoPH_output[:50] if len(campoPH_output) >= 50 else campoPH_output
        arr_sorted_campoConduc = campoConduc_output[:50] if len(campoConduc_output) >= 50 else campoConduc_output
        #Temperatura
        desviacion_media_campoTemperature, media_campoTemperature, varianza_campoTemperature, desviacion_estandar_campoTemperature, arr_ordenate_campoTemperature, table_frecuency_campoTemperature, moda_campoTemperature = statistical_calculator(
            arr_sorted_campoTemperature)
        #Humedad
        desviacion_media_campoHumidity, media_campoHumidity, varianza_campoHumidity, desviacion_estandar_campoHumidity, arr_ordenate_campoHumidity, table_frecuency_campoHumidity, moda_campoHumidity = statistical_calculator(
            arr_sorted_campoHumidity)
        #waterTemperature
        desviacion_media_campoWaterTem, media_campoWaterTem, varianza_campoWaterTem, desviacion_estandar_campoWaterTem, arr_ordenate_campoWaterTem, table_frecuency_campoWaterTem, moda_campoWaterTem= statistical_calculator(
            arr_sorted_campoWaterTem)
        #Luz
        desviacion_media_campoLight, media_campoLight, varianza_campoLight, desviacion_estandar_campoLight, arr_ordenate_campoLight, table_frecuency_campoLight, moda_campoLight= statistical_calculator(
            arr_sorted_campoLight)
        #pH
        desviacion_media_campoPH, media_campoPH, varianza_campoPH, desviacion_estandar_campoPH, arr_ordenate_campoPH, table_frecuency_campoPH, moda_campoPH= statistical_calculator(
            arr_sorted_campoPH)
        #Conductivity
        desviacion_media_campoConduC, media_campoConduc, varianza_campoConduc, desviacion_estandar_campoConduc, arr_ordenate_campoConduc, table_frecuency_campoConduc, moda_campoConduc= statistical_calculator(
            arr_sorted_campoConduc)

        print(arr_ordenate_campoTemperature)
        #Generar pdf
        generar_pdf(pd.DataFrame(table_frecuency_campoTemperature),pd.DataFrame(table_frecuency_campoHumidity),pd.DataFrame(table_frecuency_campoWaterTem),
        pd.DataFrame(table_frecuency_campoLight),pd.DataFrame(table_frecuency_campoPH),pd.DataFrame(table_frecuency_campoConduc),arr_sorted_campoHumidity, desviacion_media_campoHumidity, varianza_campoHumidity, media_campoHumidity,
        desviacion_estandar_campoHumidity,arr_sorted_campoTemperature, arr_ordenate_campoTemperature, arr_ordenate_campoTemperature,
        desviacion_media_campoTemperature, media_campoTemperature, varianza_campoTemperature, desviacion_estandar_campoTemperature,pdf_filename,
        desviacion_media_campoWaterTem, media_campoWaterTem, varianza_campoWaterTem, desviacion_estandar_campoWaterTem, arr_ordenate_campoWaterTem,
        arr_sorted_campoWaterTem,desviacion_media_campoLight, media_campoLight, varianza_campoLight, desviacion_estandar_campoLight, arr_ordenate_campoLight,
        arr_sorted_campoLight,desviacion_media_campoPH, media_campoPH, varianza_campoPH, desviacion_estandar_campoPH,arr_ordenate_campoPH,arr_sorted_campoPH,moda_campoHumidity,moda_campoTemperature
                ,moda_campoWaterTem,moda_campoLight,moda_campoPH, moda_campoConduc,arr_sorted_campoConduc, desviacion_media_campoConduC, varianza_campoConduc, media_campoConduc,
        desviacion_estandar_campoConduc)

        pdf_url = "http://localhost:6000/Public/ReporteDevly_Hydro.pdf"

        return jsonify({'url': pdf_url})


    except jwt.InvalidTokenError:
        return jsonify({'message': 'Token inválido'}), 401



@app.route('/api/documentos/<id>', methods=['DELETE'])
def eliminar_documento(id):
    documento = mongo.db.Datos.find_one({'_id': id})
    if documento:
        mongo.db.Datos.delete_one({'_id': id})
        return jsonify({'mensaje': 'Documento eliminado correctamente'})
    else:
        return jsonify({'mensaje': 'Documento no encontrado'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=400)