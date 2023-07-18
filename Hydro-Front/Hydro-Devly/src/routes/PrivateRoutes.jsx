import { Navigate } from "react-router-dom";

const PrivateRoutes = ({ children }) => {
    const authState = sessionStorage.getItem('token');
    console.log(authState)
    console.log(authState!=null)
    return authState!=null ? children : <Navigate to={'/login'} />;
  };  

export default PrivateRoutes