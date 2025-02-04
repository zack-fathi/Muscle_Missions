import { useState, useEffect } from "react";

const useAuth = () => {
  const [authenticated, setAuthenticated] = useState(false);

  useEffect(() => {
    fetch("http://localhost:5002/api/accounts/auth/", { credentials: "include" })
      .then((response) => response.json()) // Parse JSON response
      .then((data) => {
        if (data.logged_in) {
          setAuthenticated(true);
        }
      })
      .catch(() => setAuthenticated(false));
  }, []);

  return authenticated;
};

export default useAuth;
