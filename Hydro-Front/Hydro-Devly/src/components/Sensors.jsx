import React, { useEffect, useState } from "react";

export default function Sensors() {
    const [sensorData, setSensorData] = useState([
      { name: "Temperature", value: 0, unit: "°C", safeRange: [18, 40] },
      { name: "Humidity", value: 0, unit: "%", safeRange: [40, 60] },
      { name: "Altitude", value: 0, unit: "m", safeRange: [0, 500] },
      { name: "Pressure", value: 0, unit: "atm", safeRange: [0, 70] },
      { name: "CO2", value: 0, unit: "ppm", safeRange: [400, 700] },
    ]);
  
    const [reportURL, setReportURL] = useState(null);
  
    useEffect(() => {
      const socket = new WebSocket("ws://192.168.0.15:5000");
      socket.onmessage = (event) => {
        try {
          const mensajeJSON = event.data;
          const mensajeObjeto = JSON.parse(mensajeJSON);
          console.log("Mensaje recibido:", mensajeObjeto);
  
          setSensorData((prevSensorData) => {
            const updatedSensorData = prevSensorData.map((sensor) => {
              const matchingKey = Object.keys(mensajeObjeto).find(
                (key) => key.toLowerCase() === sensor.name.toLowerCase()
              );
              if (matchingKey) {
                return {
                  ...sensor,
                  value: mensajeObjeto[matchingKey],
                };
              }
              return sensor;
            });
  
            return updatedSensorData;
          });
        } catch (error) {
          console.error("Error al analizar el mensaje JSON:", error);
        }
      };
  
      socket.onopen = () => {
        console.log("Conexión establecida con el servidor WebSocket");
      };
  
      return () => {
        socket.close();
      };
    }, []);
  
    const isSafe = (sensor) => {
      const [min, max] = sensor.safeRange;
      return sensor.value >= min && sensor.value <= max;
    };
  
    const handleDownloadReport = async () => {
      try {
        const token = localStorage.getItem("token");
        console.log("obtengo el token de localstorage que es:", token);
        const response = await fetch("http://18.212.178.176:5000/api/calcular", {
          headers: {
            Authorization: `${token}`,
          },
        });
        const data = await response.json();
        console.log("Respuesta de la API:", data);
        const newWindow = window.open(data, "_blank");
        if (newWindow) {
          newWindow.opener = null;
        }
      } catch (error) {
        console.error("Error al realizar la petición GET:", error);
      }
    };
  
    useEffect(() => {
      if (reportURL) {
        window.open(reportURL, "_blank");
        setReportURL(null);
      }
    }, [reportURL]);
  
    return (
      <div>
        <div className="flex flex-col justify-center items-center space-y-6">
          <h1 className="text-4xl font-bold">Data Analytics</h1>
        </div>
        <div className="flex flex-col gap-2">
          {sensorData.map((sensor) => (
            <div
              className={`bg-gray-200 p-2 ${
                isSafe(sensor) ? "text-green-600" : "text-red-600"
              }`}
              key={sensor.name}
            >
              <h2 className="text-lg font-semibold">{sensor.name}</h2>
              <p className="text-xl">
                {sensor.value} {sensor.unit}
              </p>
              <p className="text-sm">
                {isSafe(sensor) ? "Safe" : "Unsafe for humans"}
              </p>
            </div>
          ))}
          <button
            className="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded flex items-center justify-center"
            onClick={handleDownloadReport}
          >
            <svg
              className="fill-current w-4 h-4 mr-2"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
            >
              <path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z" />
            </svg>
            <span>Download Report</span>
          </button>
        </div>
        {reportURL && (
          <script
            dangerouslySetInnerHTML={{
              __html: `
                if (window.opener) {
                  window.opener.open("${reportURL}", "_blank");
                }
              `,
            }}
          />
        )}
      </div>
    );
  }