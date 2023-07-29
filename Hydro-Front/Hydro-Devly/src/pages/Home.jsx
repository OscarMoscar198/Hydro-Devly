import {useEffect, useState} from 'react';
import {
    Chart as ChartJS,
    BarElement,
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement,
    Tooltip,
    Legend,
} from 'chart.js';
import {Bar, Line} from 'react-chartjs-2';
import "../assets/styles/home.css"
import HomeSidebar from '../components/HomeSidebar.jsx';
import GaugeMeter from "../components/GaugeMeter.jsx";


ChartJS.register(
    BarElement, LineElement, CategoryScale, LinearScale, PointElement, Tooltip, Legend,
)

const Home = () => {
    const [sensorData, setSensorData] = useState([
        {name: "WaterTem", value: 0, unit: "°C"},
        {name: "Temperature", value: 0, unit: "°C"},
        {name: "Humedity", value: 0, unit: "%"},
        {name: "Light", value: 0, unit: "lux"},
        {name: "pH", value: 0, unit: "pH"},
        {name: "Conduc", value: 0, unit: "S"},
    ]);

    useEffect(() => {
        const socket = new WebSocket("ws://18.206.113.60:4000");

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

    const getColorForSensor = (sensorName) => {
        switch (sensorName) {
            case "WaterTem":
                return 'rgb(255, 99, 132)';
            case "Temperature":
                return 'rgb(255, 159, 64)';
            case "Humedity":
                return 'rgb(255, 205, 86)';
            case "Light":
                return 'rgb(75, 192, 192)';
            case "pH":
                return 'rgb(54, 162, 235)';
            case "Conduc":
                return 'rgb(153, 102, 255)';
            default:
                return "#000000"; // Default color in case the sensor name doesn't match any cases
        }
    };
    const labels = sensorData.map(sensor => sensor.name);
    const values = sensorData.map(sensor => sensor.value);
    const BarData = {
        labels: labels,
        datasets: [
            {
                label: 'sensor data',
                data: values,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                ],
                borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)',
                    'rgb(54, 162, 235)',
                    'rgb(153, 102, 255)',
                ],
                borderWidth: 1
            },
        ]
    }
    const LineData = {
        labels: labels,
        datasets: [
            {
                label: 'sensor data',
                data: values,
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            },
        ]
    }

    return (
        <div className="home-container">
            <div className="home">
                <div className="sidebar-container">
                    <HomeSidebar/>
                </div>
                <div className="main-container">
                    <div>
                        <div className="flex flex-col justify-center items-center space-y-6">
                            <h1 className="data-title">Data</h1>
                            <br/>
                        </div>
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
                        <div className="bar">
                            <Bar data={BarData}>
                            </Bar>
                        </div>
                        <div className="line">
                            <Line data={LineData}>
                            </Line>
                        </div>
                        <div className="blank"/>
                        =
                    </div>
                </div>
            </div>
        </div>
    )
        ;
}

export default Home;
