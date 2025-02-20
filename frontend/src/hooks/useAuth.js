import { useState, useEffect } from "react";

const authURL = process.env.REACT_APP_AUTH_URL;

const useAuth = () => {
  const [authenticated, setAuthenticated] = useState(null); // Start as `null`
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${authURL}/auth/`, {
      method: "GET",
      credentials: "include",
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Auth API Response:", data);
        setAuthenticated(data.logged_in);
        setLoading(false);
      })
      .catch(() => {
        setAuthenticated(false);
        setLoading(false);
      });
  }, []);

  return { authenticated, loading };
};

export default useAuth;
