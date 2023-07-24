import {useEffect, useState} from 'react';
import "../assets/styles/home.css"
import HomeSidebar from '../components/HomeSidebar.jsx';
import GaugeMeter from "../components/GaugeMeter.jsx";
// import axios from "axios";
import Chart from "../components/Chart.jsx";

const Home = () => {
    const [sensorData, setSensorData] = useState([
        {name: "Temperature", value: 29, unit: "°C"},
        {name: "Water pH", value: 17, unit: "%"},
        {name: "Air Temperature", value: 56, unit: "°C"},
        {name: "Humidity", value: 88, unit: "hPa"},
    ]);

    useEffect(() => {
        const socket = new WebSocket("ws://192.168.0.4:5000");
        socket.onmessage = (event) => {
            try {
                const mensajeJSON = event.data;
                const mensajeObjeto = JSON.parse(mensajeJSON);
                console.log("Mensaje recibido:", mensajeObjeto);

                // Actualiza el estado sensorData con los nuevos valores recibidos
                setSensorData((prevSensorData) => {
                    // Crea un nuevo array de datos de sensores actualizados
                    const updatedSensorData = prevSensorData.map((sensor) => {
                        // Busca el sensor correspondiente en el objeto recibido
                        const matchingKey = Object.keys(mensajeObjeto).find(
                            (key) => key.toLowerCase() === sensor.name.toLowerCase()
                        );
                        if (matchingKey) {
                            // Actualiza el valor del sensor con el valor correspondiente del objeto
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

    const getColorForSensor = (sensorName) => {
        switch (sensorName) {
            case "Temperature":
                return "#00FFFF";
            case "Water pH":
                return "#FFFF00";
            case "Air Temperature":
                return "#DC143C";
            case "Humidity":
                return "#8A2BE2";
            default:
                return "#000000"; // Default color in case the sensor name doesn't match any cases
        }
    };

    const data = [
        {
            waterTemperature: Math.floor(Math.random() * 100) + 1,
            waterPh: Math.floor(Math.random() * 100) + 1,
            airTemperature: Math.floor(Math.random() * 100) + 1,
            airHumidity: Math.floor(Math.random() * 100) + 1
        },
        {
            waterTemperature: Math.floor(Math.random() * 100) + 1,
            waterPh: Math.floor(Math.random() * 100) + 1,
            airTemperature: Math.floor(Math.random() * 100) + 1,
            airHumidity: Math.floor(Math.random() * 100) + 1
        },
        {
            waterTemperature: Math.floor(Math.random() * 100) + 1,
            waterPh: Math.floor(Math.random() * 100) + 1,
            airTemperature: Math.floor(Math.random() * 100) + 1,
            airHumidity: Math.floor(Math.random() * 100) + 1
        },
        // Add more sensor data objects here
    ];
    return (
        <div className="home-container">
            <div className="home">
                <div className="sidebar-container">
                    <HomeSidebar/>
                </div>
                <div className="main-container">
                    <div>
                        <div>
                            <div className="flex flex-col justify-center items-center space-y-6">
                                <h1 className="data-title">Data Analytics</h1>
                                <h3 className="sensor-subtitle">sensors</h3>
                                <br/>
                            </div>
                            <div className="cards">
                                {sensorData.map((sensor) => (
                                    <div className="bg-white p-4" key={sensor.name}>
                                        <h2 className="text-lg font-semibold">{sensor.name}</h2>
                                        <p className="text-xl">
                                            {sensor.value} {sensor.unit}
                                        </p>
                                    </div>
                                ))}
                            </div>
                        </div>
                        <div className="gauge-meter-group">
                            {sensorData.map((sensor) => (
                                <GaugeMeter
                                    key={sensor.name}
                                    value={sensor.value}
                                    label={sensor.name}
                                    color={getColorForSensor(sensor.name)}
                                />
                            ))}
                        </div>
                        <Chart data={data}/>
                        <div className="blank">

                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Home;
