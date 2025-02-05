import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import { Container, Button, Alert, Spinner } from "react-bootstrap";
import Layout from "../../components/Layout";
import WorkoutTable from "../../components/WorkoutTable";

function ViewGeneratedWorkouts() {
  const location = useLocation();

  // Grab formData from state or fallback to sessionStorage
  const storedFormData = JSON.parse(sessionStorage.getItem("formData") || "{}");
  const formData = location.state?.formData || storedFormData;

  const [workoutDays, setWorkoutDays] = useState([]);
  const [loading, setLoading] = useState(false);

  // Keep track of login status
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Decide if it's a split
  const isSplit = formData.frequency !== "";

  // On mount: fetch the workout & check login status
  useEffect(() => {
    if (formData && Object.keys(formData).length > 0) {
      fetchWorkouts();
    } else {
      console.warn("⚠️ No form data found. Can't fetch workout.");
    }

    // Check login status
    checkLoginStatus();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const fetchWorkouts = async () => {
    setLoading(true);
    try {
      const endpoint = isSplit
        ? "http://localhost:5001/api/workouts/split/"
        : "http://localhost:5001/api/workouts/day/";

      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error("Workout generation failed");
      }

      const data = await response.json();
      const newDays = data.days || [];

      setWorkoutDays(newDays);
      sessionStorage.setItem("generatedWorkouts", JSON.stringify(data));

      console.log("✅ New Workout Data:", data);
    } catch (error) {
      console.error("❌ Error fetching workout:", error);
    } finally {
      setLoading(false);
    }
  };

  const checkLoginStatus = async () => {
    try {
      const res = await fetch("http://localhost:5002/api/accounts/auth/", {
        credentials: "include", // if you need cookies
      });
      if (res.ok) {
        const data = await res.json();
        setIsLoggedIn(data.logged_in); // or whatever field your backend returns
      } else {
        setIsLoggedIn(false);
      }
    } catch (error) {
      console.error("❌ Error checking login status:", error);
      setIsLoggedIn(false);
    }
  };

  // "Regenerate" means a fresh fetch
  const handleRegenerate = () => {
    fetchWorkouts();
  };

  const handleSaveWorkout = async () => {
    try {
      const payload = { workouts: { days: workoutDays } };
      const response = await fetch("http://localhost:5001/api/workouts/save/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(payload),
      });

      if (response.ok) {
        alert("✅ Workout saved!");
      } else {
        alert("❌ Failed to save workout.");
      }
    } catch (error) {
      console.error("❌ Error saving workout:", error);
    }
  };

  return (
    <Layout>
      <Container className="mt-4">
        <h2 className="text-center mb-4">
          {isSplit
            ? "Here is your Multi-Day Workout Split!"
            : "Here is your Generated Workout!"}
        </h2>

        {loading ? (
          <div className="text-center">
            <Spinner animation="border" role="status" />
          </div>
        ) : workoutDays.length > 0 ? (
          workoutDays.map((day, index) => {
            const displayType = day.type
              ? day.type.charAt(0).toUpperCase() + day.type.slice(1)
              : "";
            return (
              <div key={index} className="mb-4">
                <h3 className="text-center">
                  {workoutDays.length > 1 ? `Day ${index + 1} - ` : ""}
                  {displayType}
                </h3>
                <WorkoutTable exercises={day.workout_data} />
              </div>
            );
          })
        ) : (
          <Alert variant="danger" className="text-center">
            No workout data available.
          </Alert>
        )}

        {/* Buttons: Regenerate + Save */}
        <div className="text-center mt-4">
          <Button
            variant="primary"
            className="me-3"
            onClick={handleRegenerate}
            disabled={loading}
          >
            🔄 Regenerate Workout
          </Button>

          <Button
            variant="success"
            onClick={handleSaveWorkout}
            disabled={loading || !isLoggedIn} 
            // <- Disable if loading or user not logged in
          >
            💾 Save Workout
          </Button>

          {!isLoggedIn && (
            <Alert variant="warning" className="text-center mt-3">
              You must be logged in to save your workout.
            </Alert>
          )}
        </div>
      </Container>
    </Layout>
  );
}

export default ViewGeneratedWorkouts;
