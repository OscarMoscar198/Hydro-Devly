import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import signupback from './../assets/Signup/signup-background.jpg';

function Signupform() {
  const navigate = useNavigate();

  const [email, setEmail] = useState('');
  const [username, setUserName] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({ email: '', password: '', username: '' });

  const validateForm = () => {
    let isValid = true;
    const updatedErrors = { email: '', password: '', username: '' };

    if (!email) {
      updatedErrors.email = 'Email is required';
      isValid = false;
    } else {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(email)) {
        updatedErrors.email = 'Invalid email format';
        isValid = false;
      }
    }

    if (!username) {
      updatedErrors.username = 'Username is required';
      isValid = false;
    }

    if (password.length < 8 || password.length > 20) {
      updatedErrors.password = 'Password must be between 8 and 20 characters';
      isValid = false;
    }

    setErrors(updatedErrors);
    return isValid;
  };

  const registerHandler = (event) => {
    event.preventDefault();

    if (validateForm()) {
      const user = {
        email,
        username,
        password,
      };

      axios
        .post('http://18.214.206.13:400/register', user)
        .then((response) => {
          // Procesar la respuesta exitosa si es necesario
          console.log(response.data);
          navigate('/');
        })
        .catch((error) => {
          // Procesar el error si es necesario
          console.log(error);
        });
    }
  };

  return (
    <div className="relative flex flex-col justify-center min-h-screen overflow-hidden">
      <img src={signupback} className="absolute blur-sm h-screen w-screen" alt="Background" />
      <div className="w-full p-6 m-auto bg-white rounded-lg shadow-lg lg:max-w-xl  max-w-md bg-center z-10">
        <h1 className="text-2xl font-semibold text-center text-black-950">Create your account</h1>
        <form className="mt-6">
          <div className="mb-2">
            <label htmlFor="name" className="block text-sm font-semibold text-gray-800">
              Username
            </label>
            <input
              type="text"
              id="user"
              value={username}
              onChange={(e) => setUserName(e.target.value)}
              required
              autoComplete="off"
              className="shadow appearance-none block w-full px-4 py-2 mt-2 text-gray-700 bg-white border rounded-md focus:border-gray-400 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40"
              placeholder="Username"
            />
            {errors.username && <p className="text-red-500 font-semibold text-xs mt-1">{errors.username}</p>}
          </div>
          <div className="mb-2">
            <label htmlFor="email" className="block text-sm font-semibold text-gray-800">
              Email
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              autoComplete="off"
              className="shadow appearance-none block w-full px-4 py-2 mt-2 text-gray-700 bg-white border rounded-md focus:border-gray-400 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40"
              placeholder="example@hotmail.com"
            />
            {errors.email && <p className="text-red-500 font-semibold text-xs mt-1">{errors.email}</p>}
          </div>
          <div className="mb-2">
            <label htmlFor="password" className="block text-sm font-semibold text-gray-800">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              autoComplete="off"
              className="shadow appearance-none block w-full px-4 py-2 mt-2 text-gray-700 bg-white border rounded-md focus:border-gray-400 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40"
              placeholder="**********"
            />
            {errors.password && <p className="text-red-500 font-semibold text-xs mt-1">{errors.password}</p>}
          </div>
          <p className="text-xs text-gray-800 font-bold">Password needs at least 8 characters.</p>
          <div className="mt-6 flex">
            <button
              type="submit"
              onClick={registerHandler}
              className="mx-auto w-full px-4 py-2 text-white bg-blue-800 rounded-lg hover:bg-blue-500 focus:outline-none focus:bg-gray-600 font-semibold transition duration-150 ease-in"
            >
              Sign up
            </button>
          </div>
        </form>

        <p className="text-center text-xs pt-7 pb-7 text-gray-700 font-semibold">
          Already have an account?{' '}
          <a onClick={() => navigate('/')} className="font-semibold text-blue-700 underline cursor-pointer hover:text-blue-500">
            Sign in!
          </a>
        </p>
      </div>
    </div>
  );
}

export default Signupform;
