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
        const token = sessionStorage.getItem('token');
        console.log(token);
        // Fetch sensor data from the API with authorization headers
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


    const data = [
        { waterTemperature: 25, waterPh: 7.2, airTemperature: 30, airHumidity: 60 },
        { waterTemperature: 26, waterPh: 7.0, airTemperature: 28, airHumidity: 55 },
        { waterTemperature: 27, waterPh: 7.5, airTemperature: 29, airHumidity: 58 },
        // Add more sensor data objects here
    ];

    return (
        <div className="home-container">
            <div className="home">
                <div>
                    <HomeSidebar />
                </div>

                {isLoading ? (
                    <p>Loading...</p>
                ) : (
                    <div>
                        <div className="card-group">
                            <Card title="Water Temperature" value={10} />
                            <Card title="Water pH" value={10}/>
                            <Card title="Air Temperature" value={10}/>
                            <Card title="Air Humidity" value={10}/>
                        </div>
                        <div className="gauge-meter-group">
                            <GaugeMeter value={10} label="Water Temperature" color="#00FFFF" />
                            <GaugeMeter value={10} label="Water pH" color="#FFFF00" />
                            <GaugeMeter value={10} label="Air Temperature" color="#DC143C" />
                            <GaugeMeter value={10} label="Air Humidity" color="#8A2BE2" />
                        </div>
                        <Chart data={data}/>
                    </div>
                )}
            </div>
        </div>
    );
}

export default Home;
