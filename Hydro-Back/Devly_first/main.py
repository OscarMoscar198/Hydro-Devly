import serial
import time
import json
import asyncio
import websockets

arduino = serial.Serial("COM9", 9600)
time.sleep(5)

async def send_sensor_data():
    async with websockets.connect('ws://10.11.2.229:5000') as websocket: ##conexion al servidor
        while True:  # Bucle infinito para enviar datos continuamente
            val = arduino.readline().decode('ascii').strip()
            print("Cadena principal:", val)
            print("******************************************************")

            separado = val.split(",")

            if len(separado) == 6:

                dht11Temperature, dht11Humidity, ds18b20Temperature, ldrValue, phValue, tdsValue = separado
                print("temperature:", dht11Temperature)
                print("humedity", dht11Humidity)
                print("waterTem:", ds18b20Temperature)
                print("light", ldrValue)
                print("pH", phValue)
                print("conduc:", tdsValue)

                # Datos que deseas enviar en la solicitud POST
                data = {
                    'waterTem': ds18b20Temperature,
                    'temperature': dht11Temperature,
                    'humedity': dht11Humidity,
                    'light': ldrValue,
                    'pH': phValue,
                    'conduc': tdsValue
                }
                # Convertir los datos a formato JSON
                json_data = json.dumps(data)

                try:
                    await websocket.send(json_data)
                    print('Datos enviados a través de WebSocket')
                except websockets.exceptions.ConnectionClosed:
                    print('Error: La conexión WebSocket está cerrada')
                    break

            else:
                print("La cadena recibida no tiene el formato esperado.")
            
            # Esperar antes de enviar los próximos datos (por ejemplo, 1 segundo)
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_sensor_data())