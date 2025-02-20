import React from "react";
import { Container, Row, Col, Card } from "react-bootstrap";
import FormComponent from "../../components/FormComponent";
import Layout from "../../components/Layout";

const authURL = process.env.REACT_APP_AUTH_URL;

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

  const handleSubmit = async (event) => {
    event.preventDefault();
  
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
  
    if (data.new !== data.new2) {
      alert("New passwords do not match.");
      return;
    }
  
    try {
      const response = await fetch(`${authURL}/edit_password/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
          password: data.password,
          new_password: data.new,
        }),
      });
  
      const result = await response.json();
      if (response.ok) {
        alert("Password changed successfully!");
        window.location.href = "/accounts/login/";
      } else {
        alert(result.error);
      }
    } catch (error) {
      console.error("Password change error:", error);
    }
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
            </Col>
          </Row>
        </Container>
      </div>
    </Layout>
  );
}

export default ChangePassword;
