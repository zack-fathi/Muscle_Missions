import React, { useState } from "react";
import { Container } from "react-bootstrap";
import Layout from "../components/Layout";
import WorkoutForm from "../components/WorkoutForm";

function WorkoutPage({ title, showDaysPerWeek }) {
  const [formData, setFormData] = useState({
    frequency: "",
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
    console.log(`${title} Form Submitted:`, formData);
    // Add backend logic here
  };

  const fields = [
    ...(showDaysPerWeek
      ? [
          {
            type: "select",
            label: "How many days per week would you like to workout?",
            name: "frequency",
            value: formData.frequency,
            placeholder: "Select frequency",
            options: [
              { value: "2", label: "2 days" },
              { value: "3", label: "3 days" },
              { value: "4", label: "4 days" },
              { value: "5", label: "5 days" },
              { value: "6", label: "6 days" },
            ],
            required: true,
          },
        ]
      : []),
    {
      type: "select",
      label: "What kind of muscle group would you like to hit?",
      name: "muscleSplit",
      value: formData.muscleSplit,
      placeholder: "Select muscle group",
      options: [
        { value: "full", label: "Full-body" },
        { value: "upper", label: "Upper-body" },
        { value: "legs", label: "Lower-body" },
        { value: "push", label: "Push" },
        { value: "pull", label: "Pull" },
        { value: "arms", label: "Arms" },
        { value: "chest", label: "Chest" },
        { value: "back", label: "Back" },
        { value: "shoulders", label: "Shoulders" },
      ],
      required: true,
    },
    {
      type: "checkbox",
      label: "What kind of equipment do you have access to or want to use?",
      name: "equipment",
      options: [
        { value: "barbell", label: "Barbells" },
        { value: "dumbbell", label: "Dumbbells" },
        { value: "bodyweight", label: "Bodyweight" },
        { value: "machine", label: "Machines" },
      ],
    },
    {
      type: "select",
      label: "How long do you want your workouts to be?",
      name: "time",
      value: formData.time,
      placeholder: "Select duration",
      options: [
        { value: "30", label: "30 minutes" },
        { value: "45", label: "45 minutes" },
        { value: "60", label: "1 hour" },
        { value: "75", label: "1 hour 15 minutes" },
        { value: "90", label: "1 hour 30 minutes" },
        { value: "105", label: "1 hour 45 minutes" },
        { value: "120", label: "2 hours" },
      ],
      required: true,
    },
    {
      type: "checkbox",
      label: "Are there any movements you are unable to do?",
      name: "limitations",
      options: [
        { value: "squat", label: "Squats" },
        { value: "deadlift", label: "Deadlifts" },
        { value: "lunge", label: "Lunges" },
        { value: "press", label: "Benching" },
        { value: "vertical-press", label: "Overhead Pressing" },
      ],
    },
  ];

  return (
    <Layout>
      <Container className="mt-5">
        <WorkoutForm
          title={title}
          fields={fields}
          onChange={handleChange}
          onSubmit={handleSubmit}
        />
      </Container>
    </Layout>
  );
}

export default WorkoutPage;
