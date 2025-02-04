import { useState, useEffect } from "react";

const useAuth = () => {
  const [authenticated, setAuthenticated] = useState(null); // Start as `null`
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:5002/api/accounts/auth/", {
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
