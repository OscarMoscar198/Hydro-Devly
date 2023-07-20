import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Signup from './pages/Signup'
import Login from './pages/Login'
import Home from './pages/home'
import PrivateRoutes from './routes/PrivateRoutes'


function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/*' element={<Login />}></Route>
        <Route path='/login' element={<Login />}></Route>
        <Route path='/signup' element={<Signup />}></Route>
          {/*<Route path='/home' element={<Home />}></Route>*/}
        <Route path='/home' element={<PrivateRoutes><Home /></PrivateRoutes>}></Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
