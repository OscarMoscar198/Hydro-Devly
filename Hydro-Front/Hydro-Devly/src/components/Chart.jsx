import React from 'react';
import { CartesianGrid, Line, LineChart, XAxis, YAxis } from 'recharts';
import '../assets/styles/chart.css'

// eslint-disable-next-line react/prop-types
const Chart = ({ data }) => {
    return (
        <LineChart className='chart' width={1225} height={300} data={data}>
            <XAxis dataKey="name" />
            <YAxis />
            <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
            <Line type="monotone" dataKey="waterTemperature" stroke="#8884d8" name="Water Temperature" />
            <Line type="monotone" dataKey="waterPh" stroke="#82ca9d" name="Water pH" />
            <Line type="monotone" dataKey="airTemperature" stroke="#ff0000" name="Air Temperature" />
            <Line type="monotone" dataKey="airHumidity" stroke="#00ff00" name="Air Humidity" />
        </LineChart>
    );
};

export default Chart;
