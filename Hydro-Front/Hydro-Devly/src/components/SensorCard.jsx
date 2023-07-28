import {useEffect, useState} from 'react';
import "../assets/styles/home.css"


const SensorCard = () => {
    const [sensorData, setSensorData] = useState([
        {name: "Water Temperature", value: 0, unit: "°C"},
        {name: "Temperature", value: 0, unit: "°C"},
        {name: "Humidity", value: 0, unit: "%"},
        {name: "Light", value: 0, unit: "lux"},
        {name: "Water pH", value: 0, unit: "pH"},
        {name: "Conduct", value: 0, unit: "S"},
    ]);

    useEffect(() => {
        const socket = new WebSocket("ws://localhost:4000");

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


    return (
        <div>
            <div className="cards">
                {sensorData.map((sensor) => (
                    <div className="bg-white p-4" key={sensor.name}>
                        <h2 className="text-lg">{sensor.name}</h2>
                        <p className="text-xl">
                            {sensor.value} {sensor.unit}
                        </p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default SensorCard;
