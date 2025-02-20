import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const authURL = process.env.REACT_APP_AUTH_URL;

function Logout() {
  const navigate = useNavigate();

  useEffect(() => {
    fetch(`${authURL}/logout/`, {
      method: "POST",
      credentials: "include",
    })
      .then((response) => {
        if (response.ok) {
          alert("Logout successful!");
          navigate("/accounts/login/");
        } else {
          alert("Logout failed.");
        }
      })
      .catch((error) => console.error("Logout error:", error));
  }, [navigate]);

}

export default Logout;
