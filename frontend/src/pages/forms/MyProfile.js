import React, { useEffect, useState } from "react";
import {
  Container,
  Row,
  Col,
  Card,
  Form,
  Button,
  FormControl,
  FormLabel,
  FormGroup,
} from "react-bootstrap";
import Layout from "../../components/Layout";


const activity_map = {
  na: "Sedentary (0-2 hours per week of activity)",
  la: "Lightly active (2-3 hours per week of activity)",
  ma: "Moderately active (3-5 hours per week of activity)",
  va: "Very active (5+ days per week of activity)",
};

const authURL = process.env.REACT_APP_AUTH_URL;

function MyProfile({ logoSrc }) {
  const [userData, setUserData] = useState(null);
  const [isEditing, setIsEditing] = useState(false);

  // We'll track all relevant user info from the DB:
  const [formValues, setFormValues] = useState({
    fullname: "",
    age: "",
    height: "",
    weight: "",
    fitness_level: "",
    workout_experience: "0",
  });

  // Fetch user data once on mount
  useEffect(() => {
    fetch(`${authURL}/profile/`, {
      credentials: "include",
    })
      .then((response) => response.json())
      .then((data) => {
        setUserData(data);

        // Pre-fill form fields with data from DB
        setFormValues({
          fullname: data.fullname || "",
          age: data.age !== undefined ? data.age.toString() : "",
          height: data.height !== undefined ? data.height.toString() : "",
          weight: data.weight !== undefined ? data.weight.toString() : "",
          fitness_level: activity_map[data.fitness_level] || "",
          workout_experience:
            data.workout_experience !== undefined
              ? data.workout_experience.toString()
              : "0",
        });
      })
      .catch((error) => console.error("Error fetching user data:", error));
  }, []);

  // Update local form values (doesn't automatically save to DB)
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormValues((prev) => ({ ...prev, [name]: value }));
  };

  // When user clicks "Save Changes"
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch(
        `${authURL}/profile/`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          credentials: "include",
          body: JSON.stringify(formValues),
        }
      );

      const result = await response.json();
      if (response.ok) {
        alert("Profile updated successfully!");
        setIsEditing(false);
        // Also update userData so the read-only version is in sync
        setUserData((prev) => ({
          ...prev,
          ...formValues,
          // Convert numeric strings back to numbers if needed
          age: Number(formValues.age) || null,
          height: Number(formValues.height) || null,
          weight: Number(formValues.weight) || null,
          workout_experience: Number(formValues.workout_experience),
        }));
      } else {
        alert(result.error || "Something went wrong.");
      }
    } catch (error) {
      console.error("Error updating profile:", error);
    }
  };

  // Show a simple loading message if we haven't fetched userData yet
  if (!userData) return <div>Loading...</div>;

  return (
    <Layout>
      <div className="bg-light min-vh-100 d-flex align-items-center">
        <Container>
          <Row className="justify-content-center">
            <Col sm={6}>
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
                  <Form onSubmit={handleSubmit}>
                    <h3 className="mb-3 text-center">My Profile</h3>

                    <p className="text-muted text-center">
                      Please note that any information that was not required for
                      signup is not required here. However, providing it can
                      help LiftBot create a more personalized experience for
                      you.
                    </p>

                    <FormGroup className="mb-3">
                      <FormLabel>Full Name</FormLabel>
                      <FormControl
                        type="text"
                        name="fullname"
                        value={formValues.fullname}
                        onChange={handleChange}
                        disabled={!isEditing}
                      />
                    </FormGroup>

                    <FormGroup className="mb-3">
                      <FormLabel>Age</FormLabel>
                      <FormControl
                        type="number"
                        name="age"
                        value={formValues.age}
                        onChange={handleChange}
                        disabled={!isEditing}
                      />
                    </FormGroup>

                    <FormGroup className="mb-3">
                      <FormLabel>Height (cm)</FormLabel>
                      <FormControl
                        type="number"
                        name="height"
                        value={formValues.height}
                        onChange={handleChange}
                        disabled={!isEditing}
                      />
                    </FormGroup>

                    <FormGroup className="mb-3">
                      <FormLabel>Weight (kg)</FormLabel>
                      <FormControl
                        type="number"
                        name="weight"
                        value={formValues.weight}
                        onChange={handleChange}
                        disabled={!isEditing}
                      />
                    </FormGroup>

                    <FormGroup className="mb-3">
                      <FormLabel>Fitness Level</FormLabel>
                      <Form.Select
                        name="fitness_level"
                        value={formValues.fitness_level}
                        onChange={handleChange}
                        disabled={!isEditing}
                      >
                        {Object.entries(activity_map).map(([key, label]) => (
                          <option key={key} value={key}>
                            {label}
                          </option>
                        ))}
                      </Form.Select>
                    </FormGroup>

                    <FormGroup className="mb-3">
                      <FormLabel>Gym Experience</FormLabel>
                      <Form.Select
                        name="workout_experience"
                        value={formValues.workout_experience}
                        onChange={handleChange}
                        disabled={!isEditing}
                      >
                        <option value="0">Beginner (0-1 years)</option>
                        <option value="1">Intermediate (1-3 years)</option>
                        <option value="2">Advanced (3+ years)</option>
                      </Form.Select>
                    </FormGroup>

                    {/* Button to toggle edit mode */}
                    {!isEditing ? (
                      <Button
                        variant="primary"
                        className="w-100"
                        onClick={() => setIsEditing(true)}
                      >
                        Edit Profile
                      </Button>
                    ) : (
                      <div className="d-flex justify-content-between">
                        <Button
                          variant="secondary"
                          onClick={() => setIsEditing(false)}
                        >
                          Cancel
                        </Button>
                        <Button variant="primary" type="submit">
                          Save Changes
                        </Button>
                      </div>
                    )}
                  </Form>
                </Card.Body>
              </Card>

              <div className="mt-3 text-center">
                <a
                  href="/accounts/edit_password/"
                  className="btn btn-outline-primary btn-sm"
                >
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
