import React, { useEffect, useState } from "react";
import { Container, Row, Col, Card, Button } from "react-bootstrap";
import FormComponent from "../../components/FormComponent";
import Layout from "../../components/Layout";

function MyProfile({ logoSrc }) {
  const [userData, setUserData] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [formValues, setFormValues] = useState({ fullname: "", username: "", experience: "0" });

  useEffect(() => {
    fetch("http://localhost:5002/api/accounts/profile/", { credentials: "include" })
      .then((response) => response.json())
      .then((data) => {
        setUserData(data);
        setFormValues({
          fullname: data.fullname || "",
          username: data.username || "",
          experience: data.experience !== undefined ? data.experience.toString() : "0",
        });
      })
      .catch((error) => console.error("Error fetching user data:", error));
  }, []);

  const handleChange = (event) => {
    setFormValues({ ...formValues, [event.target.name]: event.target.value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch("http://localhost:5002/api/accounts/edit/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(formValues),
      });

      const result = await response.json();
      if (response.ok) {
        alert("Profile updated successfully!");
        setIsEditing(false);
        setUserData(formValues);
      } else {
        alert(result.error);
      }
    } catch (error) {
      console.error("Error updating profile:", error);
    }
  };

  if (!userData) return <div>Loading...</div>;

  const fields = [
    {
      id: "fullname",
      label: "Name",
      type: "text",
      placeholder: "Enter your full name",
      name: "fullname",
      required: true,
      value: formValues.fullname,
      onChange: handleChange,
      disabled: !isEditing,
    },
    {
      id: "username",
      label: "Username",
      type: "text",
      name: "username",
      required: true,
      value: formValues.username,
      disabled: true,
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
      value: formValues.experience,
      onChange: handleChange,
      disabled: !isEditing,
    },
  ];

  return (
    <Layout>
      <div className="bg-light min-vh-100 d-flex align-items-center">
        <Container>
          <Row className="justify-content-center">
            <Col sm={4}>
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
                  {!isEditing ? (
                    <>
                      <p><strong>Name:</strong> {userData.fullname}</p>
                      <p><strong>Experience:</strong> {fields[2].options.find(opt => opt.value === formValues.experience)?.label}</p>
                      <Button onClick={() => setIsEditing(true)} className="btn btn-primary w-100">Edit</Button>
                    </>
                  ) : (
                    <FormComponent
                      title="Edit Profile"
                      fields={fields}
                      onSubmit={handleSubmit}
                      submitButtonText="Save Changes"
                    />
                  )}
                </Card.Body>
              </Card>
              <div className="mt-3 text-center">
                <a href="/accounts/edit_password/" className="btn btn-outline-primary btn-sm">
                  Change Password
                </a>
              </div>
            </Col>
          </Row>
        </Container>
      </div>
    </Layout>
  );
}

export default MyProfile;
