import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Container } from "react-bootstrap";
import Layout from "../../components/Layout";
import WorkoutForm from "../../components/WorkoutForm";

const authURL = process.env.REACT_APP_AUTH_URL;

function GenerateWorkouts({ title, showDaysPerWeek }) {
  const navigate = useNavigate();

  // Initialize state with default difficulty = 0
  const [formData, setFormData] = useState({
    frequency: "",
    muscleSplit: "",
    equipment: [],
    time: "",
    limitations: [],
    difficulty: 0, // Default for unauthenticated users
  });

  // Fetch user difficulty level if authenticated
  useEffect(() => {
    const fetchUserDifficulty = async () => {
      try {
        const response = await fetch(
          `${authURL}/difficulty/`,
          {
            method: "GET",
            credentials: "include",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        if (response.ok) {
          const userData = await response.json();
          setFormData((prevData) => ({
            ...prevData,
            difficulty: userData.difficulty,
          }));

          console.log("✅ User difficulty:", userData.difficulty);
        }
      } catch (error) {
        console.error("❌ Failed to fetch user difficulty:", error);
      }
    };

    fetchUserDifficulty();
  }, []);

  // Handle form changes
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
      setFormData((prevData) => ({ ...prevData, [name]: value }));
    }
  };

  // Handle form submission: just pass formData forward
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Put formData in session storage if you like
    sessionStorage.setItem("formData", JSON.stringify(formData));

    // Navigate to /generated-workout with the form data
    navigate("/generated-workout/", {
      replace: true,
      state: { formData },
    });
  };

  // Define form fields
  const fields = [
    ...(showDaysPerWeek
      ? [
          {
            type: "select",
            label: "How many days per week would you like to workout?",
            name: "frequency",
            value: formData.frequency,
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
    ...(!showDaysPerWeek
      ? [
          {
            type: "select",
            label: "What kind of muscle group would you like to hit?",
            name: "muscleSplit",
            value: formData.muscleSplit,
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
        ]
      : []),
    {
      type: "checkbox",
      label: "What kind of equipment do you have access to?",
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
      options: [
        { value: "30", label: "30 minutes" },
        { value: "45", label: "45 minutes" },
        { value: "60", label: "1 hour" },
        { value: "75", label: "1 hour 15 minutes" },
        { value: "90", label: "1 hour 30 minutes" },
      ],
      required: true,
    },
    {
      type: "checkbox",
      label: "Are there any movements you cannot do?",
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

export default GenerateWorkouts;
