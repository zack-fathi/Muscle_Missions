import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

function Logout() {
  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://localhost:5002/api/accounts/logout/", {
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
