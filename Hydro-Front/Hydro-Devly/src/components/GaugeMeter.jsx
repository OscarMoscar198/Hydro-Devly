import Gauge from 'react-svg-gauge';
import '../assets/styles/gaugeMeter.css';

const GaugeMeter = ({ value, label, color }) => {
    return (
        <div className="gauge-meter">
            <Gauge
                value={value}
                width={174}
                height={140}
                label={label}
                min={0}
                max={200}
                color={color}
                topLabelStyle={{ fontSize: '17px', fontWeight: 'bold' }}
                valueLabelStyle={{ fontSize: '20px', fontWeight: 'bold' }}
                maxMinLabelStyle={{ fontSize: '16px' }}
                labelStyle={{ fontSize: '16px' }}
            />
        </div>
    );
};

export default GaugeMeter;
