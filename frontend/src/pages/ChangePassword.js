import React from "react";
import { Container, Row, Col, Card } from "react-bootstrap";
import FormComponent from "../components/FormComponent";
import Layout from "../components/Layout";

function ChangePassword({ logoSrc }) {
  const fields = [
    {
      id: "password",
      label: "Current Password",
      type: "password",
      placeholder: "Enter your current password",
      name: "password",
      required: true,
    },
    {
      id: "new",
      label: "New Password",
      type: "password",
      placeholder: "Enter your new password",
      name: "new",
      pattern: "(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",
      title:
        "Must contain at least one number, one uppercase and lowercase letter, and at least 8 characters.",
      required: true,
    },
    {
      id: "new2",
      label: "Confirm New Password",
      type: "password",
      placeholder: "Confirm your new password",
      name: "new2",
      pattern: "(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",
      title: "Must match the new password entered above.",
      required: true,
    },
  ];

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Change Password form submitted.");
    // Add your backend integration logic here
  };

  return (
    <Layout>
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
                    title="Change Password"
                    fields={fields}
                    onSubmit={handleSubmit}
                    submitButtonText="Change Password"
                  />
                </Card.Body>
              </Card>
              <div className="text-center mt-3">
                <p>
                  Need to change your user information? Click{" "}
                  <a href="/accounts/edit_more_info/" className="link-primary">
                    here!
                  </a>
                </p>
              </div>
            </Col>
          </Row>
        </Container>
      </div>
    </Layout>
  );
}

export default ChangePassword;
