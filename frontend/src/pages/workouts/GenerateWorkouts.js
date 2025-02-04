import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Container } from "react-bootstrap";
import Layout from "../../components/Layout";
import WorkoutForm from "../../components/WorkoutForm";

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
          "http://localhost:5002/api/accounts/difficulty/",
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
            difficulty: userData.difficulty, // Always sets difficulty (defaults to 0 if no user)
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

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    const endpoint = showDaysPerWeek
      ? "http://localhost:5001/api/workouts/split/"
      : "http://localhost:5001/api/workouts/day/";

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (!response.ok) throw new Error("Workout generation failed");

      const data = await response.json();
      console.log("✅ API Response:", data);

      // ✅ Fix: Extract workout_split if present
      const normalizedData =
        data.workout_split || (Array.isArray(data) ? data : [data]);
      console.log("📤 Sending Data to Next Page:", {
        formData,
        generatedWorkouts: normalizedData,
      });

      // ✅ Save data to sessionStorage before navigating
      sessionStorage.setItem("formData", JSON.stringify(formData));
      sessionStorage.setItem(
        "generatedWorkouts",
        JSON.stringify(normalizedData)
      );

      navigate("/generated-workout/", {
        replace: true,
        state: { formData, generatedWorkouts: normalizedData },
      });
    } catch (error) {
      console.error("❌ Error fetching workout:", error);
    }
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
