import React, { useState, useEffect } from "react";
import { Navbar, Nav, Container, NavDropdown } from "react-bootstrap";

function CustomNavbar() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [username, setUsername] = useState("");

  useEffect(() => {
    // Check if the user is authenticated
    fetch("http://localhost:5002/api/accounts/auth/", { credentials: "include" })
      .then((response) => response.json())
      .then((data) => {
        setIsAuthenticated(data.logged_in);
        // Make sure your backend includes a 'username' field in the response.
        // Adjust the following line accordingly if the field is named differently.
        setUsername(data.username || "");
      })
      .catch(() => {
        setIsAuthenticated(false);
        setUsername("");
      });
  }, []);

  const handleLogout = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch("http://localhost:5002/api/accounts/logout/", {
        method: "POST",
        credentials: "include",
      });

      if (response.ok) {
        alert("Logout successful!");
        setTimeout(() => {
          setIsAuthenticated(false);
          setUsername("");
          window.location.href = "/";
        }, 500);
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
              <NavDropdown title={username} id="user-dropdown">
                <NavDropdown.Item href="/accounts/profile/">My Profile</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item onClick={handleLogout}>Logout</NavDropdown.Item>
              </NavDropdown>
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
