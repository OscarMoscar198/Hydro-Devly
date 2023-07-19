import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import loginphoto from '../assets/Login/login_banner2.jpg';
import loginlogo from '../assets/icons/devly_icon.png';

function Loginform() {
  const navigate = useNavigate();

  const [username, setUserName] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const loginHandler = (event) => {
    event.preventDefault();

    const user = {
      username,
      password,
    };

    axios
      .post('http://localhost:400/login', user)
      .then((response) => {
        sessionStorage.setItem('token', response.data.token);
        // Procesar la respuesta exitosa si es necesario
        console.log(response.data);
        navigate('/home');
      })
      .catch((error) => {
        // Procesar el error si es necesario
        console.log(error);
        setError('Invalid username or password');
      });
  };

  return (
    <div className="w-full flex flex-wrap">
      <div className="w-full md:w-1/2 flex flex-col">
        <div className="flex flex-col justify-center md:justify-start my-auto pt-8 md:pt-0 px-8 md:px-24 lg:px-32">
          <img src={loginlogo} className="mx-auto w-40" alt="Logo" />
          <p className="text-center text-2xl font-semibold">Sign in into your account.</p>
          <form className="flex flex-col pt-3 md:pt-8" onSubmit={(e) => e.preventDefault()}>
            <div className="flex flex-col pt-4">
              <label htmlFor="username" className="text-base font-semibold">
                Username
              </label>
              <input
                type="text"
                id="username"
                placeholder="UsernameExample"
                autoComplete="off"
                onChange={(e) => setUserName(e.target.value)}
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mt-1 leading-tight focus:shadow-outline focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40"
              />
            </div>

            <div className="flex flex-col pt-4">
              <label htmlFor="password" className="text-base font-semibold">
                Password
              </label>
              <input
                type="password"
                id="password"
                value={password}
                placeholder="*************"
                maxLength={20}
                minLength={8}
                autoComplete="off"
                onChange={(e) => setPassword(e.target.value)}
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mt-1 leading-tight focus:shadow-outline focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40"
              />
            </div>

            {error && <p className="text-red-500 font-semibold text-xs mt-2">{error}</p>}

            <input
              type="submit"
              value="Sign in"
              onClick={loginHandler}
              className="bg-blue-800 text-white font-bold text-base hover:bg-blue-500 p-2 mt-8 rounded-md transition duration-150 ease-in"
            />
          </form>
          <div className="text-center pt-12 pb-12">
            <p className="text-base font-semibold">
              Don´t have an account yet?{' '}
              <a onClick={() => navigate('/Signup')} className="underline font-semibold text-blue-700 cursor-pointer hover:text-blue-500">
                Sign up!
              </a>
            </p>
          </div>
        </div>
      </div>

      <div className="w-1/2 shadow-2xl">
        <img className="object-cover w-full h-screen hidden md:block" src={loginphoto} alt="Background" />
      </div>
    </div>
  );
}

export default Loginform;
