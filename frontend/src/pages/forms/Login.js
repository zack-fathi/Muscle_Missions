import React from "react";
import { Container, Row, Col, Card } from "react-bootstrap";
import FormComponent from "../../components/FormComponent";

function Login({ logoSrc }) {
  const fields = [
    {
      id: "username",
      label: "Username",
      type: "text",
      placeholder: "Enter your username",
      name: "username",
      required: true,
    },
    {
      id: "password",
      label: "Password",
      type: "password",
      placeholder: "Enter your password",
      name: "password",
      required: true,
    },
  ];

  const handleSubmit = async (event) => {
    event.preventDefault();
  
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
  
    try {
      const response = await fetch("http://localhost:5002/api/accounts/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include", // Ensures cookies are stored
        body: JSON.stringify(data),
      });
    
      let result;
      try {
        result = await response.json();
      } catch {
        result = { error: "An unexpected error occurred" }; // Fallback for non-JSON errors
      }
    
      if (response.ok) {
        alert("Login successful!");
        window.location.href = "/";
      } else {
        alert(result.error || "Login failed. Please try again.");
      }
    } catch (error) {
      console.error("Login error:", error);
      alert("Network error. Please check your connection and try again.");
    }    
  };
  
  return (
    <div className="bg-light min-vh-100 d-flex align-items-center">
      <Container>
        <Row className="justify-content-center">
          <Col sm={4}>
            {/* Logo */}
            <div className="text-center">
              {logoSrc && (
                <img
                  src={logoSrc}
                  alt="Logo"
                  className="mb-4"
                  style={{ maxWidth: "150px" }}
                />
              )}
            </div>
            <Card>
              <Card.Body>
                <FormComponent
                  title="Sign In"
                  fields={fields}
                  onSubmit={handleSubmit}
                  submitButtonText="Login"
                />
              </Card.Body>
            </Card>
            <div className="mt-3 text-center">
              <p>
                Don't have an account?{" "}
                <a href="/accounts/create/" className="btn btn-outline-primary btn-sm">
                  Sign Up!
                </a>
              </p>
              <p>
                Or <a href="/">continue as a guest</a>.
              </p>
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Login;
