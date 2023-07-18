#include <ArduinoJson.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <DHT.h>

#define DHTPIN 6
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
OneWire ourWire(5);
DallasTemperature sensors(&ourWire);

// Variables para los sensores analógicos
int pHSense = A0;
int ldrSense = A1;
int tdsSense = A2;
int samples = 10;
float adc_resolution = 1024.0;
float tdsValue;

// Variables para control de ventilador y luces LED
int ventiladorPin = 7;
int ledPin = 8;
float temperaturaMaxima = 30.0; // Temperatura máxima para encender el ventilador
int ldrUmbral = 400; // Valor umbral del sensor LDR para encender las luces LED

bool ventiladorActivado = false;
bool lucesLEDActivadas = false;

void setup()
{
  Serial.begin(9600);
  dht.begin();
  sensors.begin();
  pinMode(ventiladorPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  float ds18b20Temperature = readDS18B20Temperature();
  float dht11Temperature, dht11Humidity;
  readDHT11Data(dht11Temperature, dht11Humidity);
  int ldrValue = readLDRValue();
  float phValue = readPHValue();
  float tdsValue = readTDSValue();

  // Crear un objeto JSON
  DynamicJsonDocument jsonDocument(200);
  jsonDocument["ds18b20_temperatura"] = ds18b20Temperature;
  jsonDocument["dht11_temperatura"] = dht11Temperature;
  jsonDocument["dht11_humedad"] = dht11Humidity;
  jsonDocument["ldr_valor"] = ldrValue;
  jsonDocument["ph_valor"] = phValue;
  jsonDocument["tds_valor"] = tdsValue;

  // Convertir el objeto JSON en una cadena JSON
  String jsonString;
  serializeJson(jsonDocument, jsonString);

  // Imprimir en el monitor serie
  Serial.println(jsonString);

  // Control de ventilador y luces LED
  if (dht11Temperature > temperaturaMaxima && !ventiladorActivado)
  {
    digitalWrite(ventiladorPin, HIGH); // Encender el ventilador si la temperatura es alta
    ventiladorActivado = true;
  }
  else if (dht11Temperature <= temperaturaMaxima && ventiladorActivado)
  {
    digitalWrite(ventiladorPin, LOW); // Apagar el ventilador si la temperatura es baja
    ventiladorActivado = false;
  }

  if (ldrValue < ldrUmbral && !lucesLEDActivadas)
  {
    digitalWrite(ledPin, HIGH); // Encender las luces LED si la intensidad de luz es baja
    lucesLEDActivadas = true;
  }
  else if (ldrValue >= ldrUmbral && lucesLEDActivadas)
  {
    digitalWrite(ledPin, LOW); // Apagar las luces LED si la intensidad de luz es alta
    lucesLEDActivadas = false;
  }

  delay(5000);
}

float readDS18B20Temperature()
{
  sensors.requestTemperatures();
  float temperature = sensors.getTempCByIndex(0);
  Serial.print("Temperatura ds18b20 = ");
  Serial.print(temperature);
  Serial.println(" °C");
  return temperature;
}

void readDHT11Data(float &temperature, float &humidity)
{
  temperature = dht.readTemperature();
  humidity = dht.readHumidity();

  Serial.print("Humedad dht11: ");
  Serial.print(humidity);
  Serial.println(" %");
  Serial.print("Temperatura dht11: ");
  Serial.print(temperature);
  Serial.println(" °C");
}

int readLDRValue()
{
  int value = analogRead(ldrSense);
  Serial.print("Intensidad de luz: ");
  Serial.println(value);
  return value;
}

float readPHValue()
{
  int measurings = 0;
  for (int i = 0; i < samples; i++)
  {
    measurings += analogRead(pHSense);
    delay(100);
  }

  float voltage = 5 / adc_resolution * measurings / samples;
  float phValue = 7 + ((2.5 - voltage) / 0.18);

  Serial.print("pH = ");
  Serial.println(phValue);

  return phValue;
}

float readTDSValue()
{
  int sensorValue = analogRead(tdsSense);
  float calibrationFactor = 0.5;
  float tdsValue = sensorValue * calibrationFactor;

  Serial.print("TDS Value (ppm): ");
  Serial.println(tdsValue, 2);

  return tdsValue;
}
