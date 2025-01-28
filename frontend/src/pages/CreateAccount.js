import React from "react";
import { Container, Row, Col, Card } from "react-bootstrap";
import FormComponent from "../components/FormComponent";

function CreateAccount({ logoSrc }) {
  const fields = [
    {
      id: "fullname",
      label: "Name",
      type: "text",
      placeholder: "Enter your full name",
      name: "fullname",
      required: true,
    },
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
      pattern: "(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",
      title: "Must contain at least one number, one uppercase and lowercase letter, and at least 8 characters.",
      required: true,
    },
    {
      id: "confirm-password",
      label: "Confirm Password",
      type: "password",
      placeholder: "Confirm your password",
      name: "confirm-password",
      pattern: "(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",
      title: "Must match the password entered above.",
      required: true,
    },
  ];

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Account creation form submitted.");
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
                  title="Create an Account"
                  fields={fields}
                  onSubmit={handleSubmit}
                  submitButtonText="Sign Up"
                />
              </Card.Body>
            </Card>
            <div className="mt-3 text-center">
              <p>
                Have an account?{" "}
                <a href="/accounts/login/" className="btn btn-outline-primary btn-sm">
                  Sign In Here!
                </a>
              </p>
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default CreateAccount;
