import React from 'react'
import { Link } from "react-router-dom";
import Sensors from '../components/Sensors';
import { MyResponsiveBar } from '../components/graphics/Bar';
import { MyResponsiveLine } from '../components/graphics/Line';
import loginlogo from '../assets/icons/devly_icon.png';

function Home() {
  return (
    <div className="min-h-screen flex font-global">
        {/* Logo en la esquina superior izquierda */}
        <div className="absolute top-0 left-0 p-4">
          <Link to={"/"}>
            <img src={loginlogo} alt="Logo" className="h-16" />
          </Link>
        </div>
        {/* Sección izquierda */}
        <div className="w-1/2 flex justify-center items-center">
          <div className="bg-white p-4 w-3/5 rounded-md text-black">
            <Sensors />
          </div>
        </div>
        {/* Sección derecha */}
        <div className="w-1/2 flex flex-col justify-center items-center text-black overflow-hidden">
          <div className="flex bg-white my-2 w-4/5 h-1/2 rounded-md">
            <MyResponsiveBar />
          </div>
          <div className="flex bg-white my-2 w-4/5 h-1/2 rounded-md">
            <MyResponsiveLine />
          </div>
        </div>
      </div>
  );
}

export default Home