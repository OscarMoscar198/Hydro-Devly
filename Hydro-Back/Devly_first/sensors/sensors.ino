#include <ArduinoJson.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <DHT.h>
#include <SD.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define DHTPIN 6
#define DHTTYPE DHT11
 
DHT dht(DHTPIN, DHTTYPE);
OneWire ourWire(5);
DallasTemperature sensors(&ourWire);

// Dirección I2C del LCD
const int lcdAddress = 0x27;

// Configuración del LCD
const int lcdColumns = 16;
const int lcdRows = 2;

// Inicializar el objeto LCD
LiquidCrystal_I2C lcd(lcdAddress, lcdColumns, lcdRows);

// Variables para los sensores analógicos
int pHSense = A0;
int ldrSense = A1;
int tdsSense = A2;
int samples = 10;
float adc_resolution = 1024.0;
float tdsValue;

unsigned long previousMillis = 0;
const unsigned long interval = 3000; // Intervalo de tiempo para cambiar los datos en el LCD (en milisegundos)
int dataMode = 0; // Variable para controlar el modo de datos en el LCD

void setup()
{
  Serial.begin(9600);
  sensors.begin();
  lcd.begin(lcdColumns, lcdRows);
  lcd.backlight();
}

void loop()
{
  unsigned long currentMillis = millis();

  // Verificar si ha pasado el intervalo de tiempo
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // Incrementar el modo de datos
    dataMode++;
    if (dataMode > 2) {
      dataMode = 0;
    }
  }

  float ds18b20Temperature = readDS18B20Temperature();
  float dht11Temperature, dht11Humidity;
  readDHT11Data(dht11Temperature, dht11Humidity);
  int ldrValue = readLDRValue();
  float phValue = readPHValue();
  float tdsValue = readTDSValue();

  // Mostrar los datos en el LCD
  lcd.clear();  // Limpiar el contenido anterior en el LCD
  lcd.setCursor(0, 0);  // Establecer la posición del cursor en la primera fila
  switch (dataMode) {
    case 0:
      lcd.print("Temp: ");
      lcd.print(dht11Temperature);
      lcd.print("C");
      lcd.setCursor(0, 1);  // Establecer la posición del cursor en la segunda fila
      lcd.print("Hum: ");
      lcd.print(dht11Humidity);
      lcd.print("%");
      break;
    case 1:
      lcd.print("Light: ");
      lcd.print(ldrValue);
      lcd.setCursor(0, 1);  // Establecer la posición del cursor en la segunda fila
      lcd.print("WaterTem: ");
      lcd.print(ds18b20Temperature);
      lcd.print("C");
      break;
    case 2:
      lcd.print("pH: ");
      lcd.print(phValue);
      lcd.setCursor(0, 1);  // Establecer la posición del cursor en la segunda fila
      lcd.print("Cndc: ");
      lcd.print(tdsValue);
      lcd.print("µS/cm");
      break;
  }






  Serial.println(String(dht11Temperature,2) + "," + String(dht11Humidity,2) + "," + String(ds18b20Temperature,2) + "," + String(ldrValue,2) + "," + String(phValue,2) + "," + String(tdsValue,2) );

  delay(5000);
}


float readDS18B20Temperature()
{
  sensors.requestTemperatures();
  float temperature = sensors.getTempCByIndex(0);
  return temperature;
}

void readDHT11Data(float &temperature, float &humidity)
{
  temperature = dht.readTemperature();
  humidity = dht.readHumidity();
}

int readLDRValue()
{
  int value = analogRead(ldrSense);
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
  float phValue = 3.5 + ((2.5 - voltage) / 0.18);
  return phValue;
}

float readTDSValue()
{
  int sensorValue = analogRead(tdsSense);
  float calibrationFactor = 5;
  float tdsValue = sensorValue * calibrationFactor;
  return tdsValue;
}