import {useEffect, useState} from 'react';
import "../assets/styles/home.css"
import HomeSidebar from '../components/HomeSidebar.jsx';
import GaugeMeter from "../components/GaugeMeter.jsx";
import axios from "axios";
import Card from "../components/Card.jsx";
import Chart from "../components/Chart.jsx";

const Home = () => {
    const [sensorData, setSensorData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        console.log(sessionStorage.getItem("token"))
        if (sessionStorage.getItem("token") != null) {
            console.log("ENTRE")
            sessionStorage.removeItem("token")

        }
    }, [])

    useEffect(() => {
        const token = sessionStorage.getItem('token');
        // console.log(token);
        axios
            .get('http://localhost:400/api/calcular', {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            })
            .then((response) => {
                console.log(response.data); // Log the response data
                setSensorData(response.data);
                setIsLoading(false);
            })
            .catch((error) => {
                console.log('Error fetching sensor data:', error);
                setIsLoading(false);
            });
    }, []);

    const waterTempRand = Math.floor(Math.random() * 100) + 1;
    const waterPhRand = Math.floor(Math.random() * 100) + 1;
    const airTempRand = Math.floor(Math.random() * 100) + 1;
    const airHumRand = Math.floor(Math.random() * 100) + 1;

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
                    {isLoading ? (
                        <p>Loading...</p>
                    ) : (
                        <div>
                            <div className="card-group">
                                <Card title="Water Temperature" value={waterTempRand}/>
                                <Card title="Water pH" value={waterPhRand}/>
                                <Card title="Air Temperature" value={airTempRand}/>
                                <Card title="Air Humidity" value={airHumRand}/>
                            </div>
                            <div className="gauge-meter-group">
                                <GaugeMeter value={waterTempRand} label="Water Temperature" color="#00FFFF"/>
                                <GaugeMeter value={waterPhRand} label="Water pH" color="#FFFF00"/>
                                <GaugeMeter value={airTempRand} label="Air Temperature" color="#DC143C"/>
                                <GaugeMeter value={airHumRand} label="Air Humidity" color="#8A2BE2"/>
                            </div>
                            {/*<Chart data={data}/>*/}
                            <div className="blank">

                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

export default Home;
