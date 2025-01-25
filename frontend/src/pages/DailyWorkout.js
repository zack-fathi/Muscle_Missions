import React, { useState } from "react";
import { Container, Card, Form, Button } from "react-bootstrap";
import Layout from "../components/Layout";

function DailyWorkout() {
  const [formData, setFormData] = useState({
    muscleSplit: "",
    equipment: [],
    time: "",
    limitations: [],
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    if (type === "checkbox") {
      setFormData((prevData) => ({
        ...prevData,
        [name]: checked
          ? [...(prevData[name] || []), value]
          : prevData[name].filter((item) => item !== value),
      }));
    } else {
      setFormData({ ...formData, [name]: value });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form Data Submitted:", formData);
    // Add logic to send form data to the backend
  };

  return (
    <Layout>
      <Container className="mt-5">
        <h2 className="text-center mb-4">
            Let’s get started! Answer a few quick questions to create a personalized workout just for you.
        </h2>

        <Card>
          <Card.Body>
            <Form onSubmit={handleSubmit}>
              {/* Muscle Split */}
              <Form.Group className="mb-3">
                <Form.Label>What kind of muscle group would you like to hit?</Form.Label>
                <Form.Select
                  name="muscleSplit"
                  value={formData.muscleSplit}
                  onChange={handleChange}
                  required
                >
                  <option value="">Select...</option>
                  <option value="full">Full-body</option>
                  <option value="upper">Upper-body</option>
                  <option value="legs">Lower-body</option>
                  <option value="push">Push</option>
                  <option value="pull">Pull</option>
                  <option value="arms">Arms</option>
                  <option value="chest">Chest</option>
                  <option value="back">Back</option>
                  <option value="shoulders">Shoulders</option>
                </Form.Select>
              </Form.Group>

              {/* Equipment */}
              <Form.Group className="mb-3">
                <Form.Label>What kind of equipment do you have access to or want to use?</Form.Label>
                {["barbell", "dumbbell", "bodyweight", "machine"].map((equipment) => (
                  <Form.Check
                    key={equipment}
                    type="checkbox"
                    id={equipment}
                    name="equipment"
                    value={equipment}
                    label={equipment.charAt(0).toUpperCase() + equipment.slice(1)}
                    onChange={handleChange}
                  />
                ))}
              </Form.Group>

              {/* Time */}
              <Form.Group className="mb-3">
                <Form.Label>How long do you want your workout to be?</Form.Label>
                <Form.Select
                  name="time"
                  value={formData.time}
                  onChange={handleChange}
                  required
                >
                  <option value="">Select...</option>
                  <option value="30">30 minutes</option>
                  <option value="45">45 minutes</option>
                  <option value="60">1 hour</option>
                  <option value="75">1 hour 15 minutes</option>
                  <option value="90">1 hour 30 minutes</option>
                  <option value="105">1 hour 45 minutes</option>
                  <option value="120">2 hours</option>
                </Form.Select>
              </Form.Group>

              {/* Limitations */}
              <Form.Group className="mb-3">
                <Form.Label>Are there any movements you are unable to do?</Form.Label>
                {["squat", "deadlift", "lunge", "press", "vertical-press"].map(
                  (limitation) => (
                    <Form.Check
                      key={limitation}
                      type="checkbox"
                      id={limitation}
                      name="limitations"
                      value={limitation}
                      label={limitation.replace("-", " ").replace(/^\w/, (c) => c.toUpperCase())}
                      onChange={handleChange}
                    />
                  )
                )}
              </Form.Group>

              <Button type="submit" variant="primary">
                Submit
              </Button>
            </Form>
          </Card.Body>
        </Card>
      </Container>
    </Layout>
  );
}

export default DailyWorkout;