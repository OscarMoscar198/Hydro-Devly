import React from 'react';
import Gauge from 'react-svg-gauge';
import '../assets/styles/gaugeMeter.css';

// eslint-disable-next-line react/prop-types
const GaugeMeter = ({ value, label, color }) => {
    return (
        <div className="gauge-meter">
            <Gauge
                value={value}
                width={250}
                height={200}
                label={label}
                min={0}
                max={100}
                color={color}
                topLabelStyle={{ fontSize: '20px', fontWeight: 'bold' }}
                valueLabelStyle={{ fontSize: '36px', fontWeight: 'bold' }}
                maxMinLabelStyle={{ fontSize: '16px' }}
                labelStyle={{ fontSize: '16px' }}
            />
        </div>
    );
};

export default GaugeMeter;
