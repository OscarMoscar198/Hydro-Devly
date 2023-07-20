import {useEffect, useState} from 'react';
import "../assets/styles/home.css"
import HomeSidebar from '../components/HomeSidebar.jsx';
import GaugeMeter from "../components/GaugeMeter.jsx";
// import axios from "axios";
import Card from "../components/Card.jsx";
// import Chart from "../components/Chart.jsx";

const Home = () => {
    const [sensorData, setSensorData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const socket = new WebSocket('ws://192.168.0.4:5000'); // Connect to the WebSocket server

        socket.onopen = () => {
            console.log('WebSocket connected');
        };

        socket.onmessage = (event) => {
            // Parse the incoming data from the server
            const data = JSON.parse(event.data);
            setSensorData(data);
            setIsLoading(false);
        };

        socket.onerror = (error) => {
            console.error('WebSocket error:', error);
        };

        socket.onclose = () => {
            console.log('WebSocket closed');
        };

        // Clean up the WebSocket connection on component unmount
        return () => {
            socket.close();
        };
    }, []);

    // const waterTempRand = Math.floor(Math.random() * 100) + 1;
    // const waterPhRand = Math.floor(Math.random() * 100) + 1;
    // const airTempRand = Math.floor(Math.random() * 100) + 1;
    // const airHumRand = Math.floor(Math.random() * 100) + 1;

    // const data = [
    //     {
    //         waterTemperature: Math.floor(Math.random() * 100) + 1,
    //         waterPh: Math.floor(Math.random() * 100) + 1,
    //         airTemperature: Math.floor(Math.random() * 100) + 1,
    //         airHumidity: Math.floor(Math.random() * 100) + 1
    //     },
    //     {
    //         waterTemperature: Math.floor(Math.random() * 100) + 1,
    //         waterPh: Math.floor(Math.random() * 100) + 1,
    //         airTemperature: Math.floor(Math.random() * 100) + 1,
    //         airHumidity: Math.floor(Math.random() * 100) + 1
    //     },
    //     {
    //         waterTemperature: Math.floor(Math.random() * 100) + 1,
    //         waterPh: Math.floor(Math.random() * 100) + 1,
    //         airTemperature: Math.floor(Math.random() * 100) + 1,
    //         airHumidity: Math.floor(Math.random() * 100) + 1
    //     },
    //     // Add more sensor data objects here
    // ];

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
                                <Card title="Water Temperature" value={sensorData?.waterTem}/>
                                <Card title="Water pH" value={sensorData?.pH}/>
                                <Card title="Air Temperature" value={sensorData?.temperature}/>
                                <Card title="Air Humidity" value={sensorData?.humedity}/>
                            </div>
                            <div className="gauge-meter-group">
                                <GaugeMeter value={sensorData?.waterTem} label="Water Temperature" color="#00FFFF"/>
                                <GaugeMeter value={sensorData?.pH} label="Water pH" color="#FFFF00"/>
                                <GaugeMeter value={sensorData?.temperature} label="Air Temperature" color="#DC143C"/>
                                <GaugeMeter value={sensorData?.humedity} label="Air Humidity" color="#8A2BE2"/>
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
