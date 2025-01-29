import React from "react";
import { Container, Row, Col, Card } from "react-bootstrap";
import FormComponent from "../../components/FormComponent";
import Layout from "../../components/Layout";

function UserInformationForm({ logoSrc }) {
  const fields = [
    {
      id: "age",
      label: "Age",
      type: "number",
      placeholder: "Enter your age",
      name: "age",
      required: true,
    },
    {
      id: "height",
      label: "Height (in inches)",
      type: "number",
      placeholder: "Enter your height",
      name: "height",
      required: true,
    },
    {
      id: "weight",
      label: "Weight (in pounds)",
      type: "number",
      placeholder: "Enter your weight",
      name: "weight",
      required: true,
    },
    {
      id: "activity-level",
      label: "Activity Level",
      type: "select",
      name: "activity_level",
      options: [
        { value: "na", label: "Sedentary (up to 2 hours a week)" },
        { value: "la", label: "Lightly Active (2-3 hours a week)" },
        { value: "ma", label: "Moderately Active (3-5 hours a week)" },
        { value: "va", label: "Very Active (5+ hours a week)" },
      ],
      required: true,
    },
    {
      id: "experience",
      label: "How experienced are you in the gym?",
      type: "select",
      name: "experience",
      options: [
        { value: "0", label: "Beginner (0-1 years experience)" },
        { value: "1", label: "Intermediate (1-3 years experience)" },
        { value: "2", label: "Advanced (3+ years experience)" },
      ],
      required: true,
    },
    {
      id: "gender",
      label: "Gender",
      type: "radio",
      name: "gender",
      options: [
        { value: "male", label: "Male" },
        { value: "female", label: "Female" },
        { value: "other", label: "Other" },
      ],
      required: true,
    },
  ];

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("User Information Form Submitted.");
    // Add your backend integration logic here
  };

  return (
    <Layout>
      <div className="bg-light min-vh-100 d-flex align-items-center">
        <Container>
          <Row className="justify-content-center">
            <Col sm={6}>
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
              <h2 className="text-center mb-4">Edit Your Information</h2>
              <Card>
                <Card.Body>
                  <FormComponent
                    title="User Information Form"
                    fields={fields}
                    onSubmit={handleSubmit}
                    submitButtonText="Submit"
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

export default UserInformationForm;
