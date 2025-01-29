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

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Login form submitted.");
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
