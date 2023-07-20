import React, { useEffect, useState } from "react";
import { ResponsiveLine } from "@nivo/line";

const MAX_DATA_POINTS = 6; // Número máximo de datos a mostrar en cada serie
const INTERVAL_SECONDS = 6; // Intervalo de tiempo en segundos

export const MyResponsiveLine = () => {
    const [data, setData] = useState([
      {
        id: "Temperature",
        color: "hsl(352, 70%, 50%)",
        data: [],
      },
      {
        id: "Pressure",
        color: "hsl(346, 70%, 50%)",
        data: [],
      },
      {
        id: "Humidity",
        color: "hsl(115, 70%, 50%)",
        data: [],
      },
      {
        id: "CO2",
        color: "hsl(303, 70%, 50%)",
        data: [],
      },
      {
        id: "Altitude",
        color: "hsl(303, 70%, 50%)",
        data: [],
      },
    ]);
  
    useEffect(() => {
      const socket = new WebSocket("ws://192.168.0.17:3000");
  
      let counter = 0; // Variable para realizar un seguimiento del tiempo transcurrido
      let interval;
  
      socket.onmessage = (event) => {
        try {
          const mensajeJSON = event.data;
          const mensajeObjeto = JSON.parse(mensajeJSON);
          console.log("Mensaje recibido:", mensajeObjeto);
  
          setData((prevData) => {
            const newData = prevData.map((item) => {
              const matchingKey = Object.keys(mensajeObjeto).find(
                (key) => key.toLowerCase() === item.id.toLowerCase()
              );
              if (matchingKey) {
                const updatedData = [
                  ...item.data,
                  {
                    x: counter,
                    y: parseFloat(mensajeObjeto[matchingKey]),
                  },
                ];
  
                // Limitar la cantidad de datos a MAX_DATA_POINTS
                if (updatedData.length > MAX_DATA_POINTS) {
                  updatedData.slice(0, updatedData.length - MAX_DATA_POINTS);
                }
  
                return {
                  ...item,
                  data: updatedData,
                };
              }
              return item;
            });
            return newData;
          });
        } catch (error) {
          console.error("Error al analizar el mensaje JSON:", error);
        }
      };
  
      socket.onopen = () => {
        console.log("Conexión establecida con el servidor WebSocket");
  
        // Iniciar intervalo para actualizar el valor del eje x cada 5 segundos
        interval = setInterval(() => {
          counter += INTERVAL_SECONDS;
        }, INTERVAL_SECONDS * 1000);
      };
  
      return () => {
        socket.close();
        clearInterval(interval);
      };
    }, []);
  
    return (
      <ResponsiveLine
        data={data}
        margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
        xScale={{ type: "linear", min: 0, max: "auto" }}
        yScale={{
          type: "linear",
          min: "auto",
          max: "auto",
          stacked: true,
          reverse: false,
        }}
        yFormat=" >-.2f"
        axisTop={null}
        axisRight={null}
        axisBottom={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
          legend: "time seg.",
          legendOffset: 36,
          legendPosition: "middle",
        }}
        axisLeft={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
          legend: "data",
          legendOffset: -40,
          legendPosition: "middle",
        }}
        pointSize={10}
        pointColor={{ theme: "background" }}
        pointBorderWidth={2}
        pointBorderColor={{ from: "serieColor" }}
        pointLabelYOffset={-12}
        useMesh={true}
        legends={[
          {
            anchor: "bottom-right",
            direction: "column",
            justify: false,
            translateX: 100,
            translateY: 0,
            itemsSpacing: 0,
            itemDirection: "left-to-right",
            itemWidth: 80,
            itemHeight: 20,
            itemOpacity: 0.75,
            symbolSize: 12,
            symbolShape: "circle",
            symbolBorderColor: "rgba(0, 0,100, .6)",
            effects: [
              {
                on: "hover",
                style: {
                  itemBackground: "rgba(0, 0, 100,.3)",
                  itemOpacity: 2,
                },
              },
            ],
          },
        ]}
      />
    );
  };