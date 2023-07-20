import React, { useState, useEffect } from "react";
import { ResponsiveBar } from "@nivo/bar";

export const MyResponsiveBar = () => {
    const [data, setData] = useState([]);
  
    const handleWebSocketMessage = (event) => {
      try {
        const messageJSON = event.data;
        const messageObject = JSON.parse(messageJSON);
        console.log("Mensaje recibido:", messageObject);
  
        setData((prevData) => {
          const newData = [
            {
              date: new Date().toLocaleTimeString().slice(0, 8), // Formatear la fecha y mostrar solo HH:MM:SS
              Temperature: messageObject.Temperature,
            },
          ];
          return [...prevData, ...newData];
        });
      } catch (error) {
        console.error("Error al analizar el mensaje JSON:", error);
      }
    };
  
    useEffect(() => {
      const socket = new WebSocket("ws://192.168.0.17:3000"); // Reemplaza con la URL de tu servidor WebSocket
  
      socket.onmessage = handleWebSocketMessage;
  
      return () => {
        socket.close();
      };
    }, []);
  
    useEffect(() => {
      const interval = setInterval(() => {
        setData((prevData) => {
          if (prevData.length >= 5) {
            return prevData.slice(1); // Limitar la longitud de los datos a 12 para evitar superposiciones
          }
          return prevData;
        });
      }, 5000);
  
      return () => {
        clearInterval(interval);
      };
    }, []);
  
    return (
      <ResponsiveBar
        data={data}
        keys={["Temperature"]}
        indexBy="date"
        margin={{ top: 50, right: 130, bottom: 50, left: 60 }}
        padding={0.3}
        valueScale={{ type: "linear" }}
        indexScale={{ type: "band", round: true }}
        colors={{ scheme: "nivo" }}
        borderColor={{ from: "color", modifiers: [["darker", 1.6]] }}
        axisTop={null}
        axisRight={null}
        axisBottom={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
          legend: "Time",
          legendPosition: "middle",
          legendOffset: 32,
        }}
        axisLeft={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
          legend: "Temperature",
          legendPosition: "middle",
          legendOffset: -40,
        }}
        labelSkipWidth={12}
        labelSkipHeight={12}
        labelTextColor={{ from: "color", modifiers: [["darker", 1.6]] }}
        animate={true}
        motionStiffness={90}
        motionDamping={15}
      />
    );
  };