import numpy as np
import pandas as pd
from pymongo import MongoClient

def get_data_from_db(collection_name, field_name, num_data):
    client = MongoClient("mongodb://127.0.0.1:27017/")
    database = client["Devly"]
    collection = database["datos"]
    filtro = {}
    proyeccion = {field_name: 1}
    cursor = collection.find(filtro, proyeccion)
    datosDB = []
    iteracion = 0
    for documento in cursor:
        valor = documento[field_name]
        if valor != '':
            valor_float = float(valor)
            datosDB.append(valor_float)
            iteracion += 1
        if iteracion == num_data:
            break
    return datosDB

def calculate_statistics(arr_sorted):
    media = np.mean(arr_sorted)
    desviacion_media = np.mean(np.abs(arr_sorted - media))
    varianza = np.var(arr_sorted)
    desviacion_estandar = np.std(arr_sorted)
    return media, desviacion_media, varianza, desviacion_estandar

def generate_frequency_table(arr_sorted, variabilidad):
    valor_min = arr_sorted[0]
    K = 1 + (3.322 * np.log10(len(arr_sorted)))
    K_round = round(K)
    R = arr_sorted[-1] - arr_sorted[0]
    A = R / K_round
    A_round = round(A + 0.1)

    datos = np.zeros((6, 6))
    df = pd.DataFrame(
        datos, columns=["LimInf", "LimSup", "Frecuencia", "Marca de clase", "LimInfExacta", "LimSupExacta"])

    df.iloc[0, 0] = valor_min
    df.iloc[0, 1] = valor_min + A_round - variabilidad

    for i in range(1, df.shape[0]):
        df.iloc[i, 0] = df.iloc[i - 1, 1] + 1
        df.iloc[i, 1] = df.iloc[i, 0] + A_round - variabilidad

    df["Frecuencia"] = [(arr_sorted >= df.iloc[i, 0]) & (arr_sorted <= df.iloc[i, 1]).sum() for i in range(df.shape[0])]
    df["Marca de clase"] = (df["LimInf"] + df["LimSup"]) / 2
    df["LimInfExacta"] = df["LimInf"] - (variabilidad / 2)
    df["LimSupExacta"] = df["LimSup"] + (variabilidad / 2)

    return df

cant_Num = int(input("Cuántos datos desea ingresar? "))

arr_humedad = get_data_from_db("datos", "Humedad", cant_Num)
arr_sorted_humedad = np.sort(arr_humedad)
print(f"Conjunto de datos NO ordenados (Humedad):\n {arr_humedad}")
print(f"Conjunto de datos Si ordenados (Humedad):\n {arr_sorted_humedad}")

arr_temperatura = get_data_from_db("datos", "Temperatura", cant_Num)
arr_sorted_temperatura = np.sort(arr_temperatura)
print(f"Conjunto de datos NO ordenados (Temperatura):\n {arr_temperatura}")
print(f"Conjunto de datos Si ordenados (Temperatura):\n {arr_sorted_temperatura}")

arr_ldr = get_data_from_db("datos", "LDR", cant_Num)
arr_sorted_ldr = np.sort(arr_ldr)
print(f"Conjunto de datos NO ordenados (LDR):\n {arr_ldr}")
print(f"Conjunto de datos Si ordenados (LDR):\n {arr_sorted_ldr}")

arr_tds = get_data_from_db("datos", "TDS", cant_Num)
arr_sorted_tds = np.sort(arr_tds)
print(f"Conjunto de datos NO ordenados (TDS):\n {arr_tds}")
print(f"Conjunto de datos Si ordenados (TDS):\n {arr_sorted_tds}")

arr_ds18b20 = get_data_from_db("datos", "DS18B20", cant_Num)
arr_sorted_ds18b20 = np.sort(arr_ds18b20)
print(f"Conjunto de datos NO ordenados (DS18B20):\n {arr_ds18b20}")
print(f"Conjunto de datos Si ordenados (DS18B20):\n {arr_sorted_ds18b20}")

arr_ph = get_data_from_db("datos", "pH", cant_Num)
arr_sorted_ph = np.sort(arr_ph)
print(f"Conjunto de datos NO ordenados (pH):\n {arr_ph}")
print(f"Conjunto de datos Si ordenados (pH):\n {arr_sorted_ph}")

media_humedad, desviacion_media_humedad, varianza_humedad, desviacion_estandar_humedad = calculate_statistics(arr_sorted_humedad)
media_temperatura, desviacion_media_temperatura, varianza_temperatura, desviacion_estandar_temperatura = calculate_statistics(arr_sorted_temperatura)
media_ldr, desviacion_media_ldr, varianza_ldr, desviacion_estandar_ldr = calculate_statistics(arr_sorted_ldr)
media_tds, desviacion_media_tds, varianza_tds, desviacion_estandar_tds = calculate_statistics(arr_sorted_tds)
media_ds18b20, desviacion_media_ds18b20, varianza_ds18b20, desviacion_estandar_ds18b20 = calculate_statistics(arr_sorted_ds18b20)
media_ph, desviacion_media_ph, varianza_ph, desviacion_estandar_ph = calculate_statistics(arr_sorted_ph)

variabilidad = 0  # Ajusta la variabilidad según tus datos

df_humedad = generate_frequency_table(arr_sorted_humedad, variabilidad)
df_temperatura = generate_frequency_table(arr_sorted_temperatura, variabilidad)
df_ldr = generate_frequency_table(arr_sorted_ldr, variabilidad)
df_tds = generate_frequency_table(arr_sorted_tds, variabilidad)
df_ds18b20 = generate_frequency_table(arr_sorted_ds18b20, variabilidad)
df_ph = generate_frequency_table(arr_sorted_ph, variabilidad)

print("Tabla de frecuencia (Humedad):\n", df_humedad)
print("Tabla de frecuencia (Temperatura):\n", df_temperatura)
print("Tabla de frecuencia (LDR):\n", df_ldr)
print("Tabla de frecuencia (TDS):\n", df_tds)
print("Tabla de frecuencia (DS18B20):\n", df_ds18b20)
print("Tabla de frecuencia (pH):\n", df_ph)
