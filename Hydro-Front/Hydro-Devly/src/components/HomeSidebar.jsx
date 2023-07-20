import "../assets/styles/homeSidebar.css";
import Loginlogo from "../assets/icons/devly_icon.png";
import HomeLogo from "../assets/Home/home.png";
import BackLogo from "../assets/Home/sign-out.png";

const HomeSidebar = () => {
    return (
        <div className="sidebar">
            <div className="logo">
                {/* Add your logo image here */}
                <img src={Loginlogo} alt="Logo" />
            </div>
            <div className="menu">
                {/* Home button */}
                <div className="menu-item">
                    {/* Add home button icon here */}
                    <img src={HomeLogo} alt="Home" />
                </div>
            </div>
            <div className="footer">
                {/* Go back button */}
                <div className="back-button">
                    {/* Add go back button icon here */}
                    <img src={BackLogo} alt="Go Back" />
                </div>
            </div>
        </div>
    );
};

export default HomeSidebar;
