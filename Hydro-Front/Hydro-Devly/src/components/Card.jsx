import React from 'react';
import "../assets/styles/card.css"

// eslint-disable-next-line react/prop-types
const Card = ({ title, value }) => {
    return (
        <div className="card">
            <h2 className="card-title">{title}</h2>
            <p className="card-value">{value}</p>
        </div>
    );
};

export default Card;
