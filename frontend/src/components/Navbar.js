import React, { useState, useEffect } from "react";
import { Navbar, Nav, Container } from "react-bootstrap";

function CustomNavbar() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    // Check if the user is authenticated
    fetch("http://localhost:5002/api/accounts/auth/", { credentials: "include" })
      .then((response) => response.json()) // Parse JSON response
      .then((data) => {
        setIsAuthenticated(data.logged_in); // Set state based on `logged_in` field
      })
      .catch(() => setIsAuthenticated(false)); // Handle fetch errors
  }, []);

  const handleLogout = async (event) => {
    event.preventDefault(); // Prevent default link behavior

    try {
      const response = await fetch("http://localhost:5002/api/accounts/logout/", {
        method: "POST",
        credentials: "include",
      });

      if (response.ok) {
        alert("Logout successful!");

        setTimeout(() => {
          setIsAuthenticated(false); // Update state to reflect logout
          window.location.href = "/"; // Redirect to index page
        }, 500); // 500ms delay to show alert
      } else {
        alert("Logout failed.");
      }
    } catch (error) {
      console.error("Logout error:", error);
    }
  };

  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="/">Muscle Missions</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarNav" />
        <Navbar.Collapse id="navbarNav">
          <Nav className="me-auto">
            <Nav.Link href="/saved_workouts/">Your Workout</Nav.Link>
            <Nav.Link href="/liftbot/">LiftBot</Nav.Link>
            {isAuthenticated && <Nav.Link href="/accounts/edit/">Edit Account</Nav.Link>}
          </Nav>
          <Nav className="ms-auto">
            {isAuthenticated ? (
              <Nav.Link href="#" onClick={handleLogout}>
                Logout
              </Nav.Link>
            ) : (
              <>
                <Nav.Link href="/accounts/login/">Login</Nav.Link>
                <Nav.Link href="/accounts/create/">Sign Up</Nav.Link>
              </>
            )}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default CustomNavbar;
