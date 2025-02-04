import React, { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { Container, Button, Alert, Spinner } from "react-bootstrap";
import Layout from "../../components/Layout";
import WorkoutTable from "../../components/WorkoutTable";

function ViewGeneratedWorkouts() {
  const navigate = useNavigate();
  const location = useLocation();

  // Restore state from sessionStorage if missing
  const savedWorkouts = JSON.parse(
    sessionStorage.getItem("generatedWorkouts") || "[]"
  );
  const savedFormData = JSON.parse(sessionStorage.getItem("formData") || "{}");

  const formData = location.state?.formData || savedFormData;

  // Extract workout_split if present in sessionStorage
  let initialGeneratedWorkouts =
    location.state?.generatedWorkouts || savedWorkouts;
  if (initialGeneratedWorkouts.workout_split) {
    initialGeneratedWorkouts = initialGeneratedWorkouts.workout_split;
  }

  const [generatedWorkouts, setGeneratedWorkouts] = useState(
    initialGeneratedWorkouts
  );

  const [loading, setLoading] = useState(false); // Loading state

  console.log("📥 Received Data from Previous Page:", {
    formData,
    generatedWorkouts,
  });

  // Check if it's a multi-day split
  const isSplit = Array.isArray(generatedWorkouts) && generatedWorkouts.length > 1;

  // Function to fetch workouts if missing
  const fetchWorkouts = async () => {
    if (!generatedWorkouts || generatedWorkouts.length === 0) return; // Skip fetching if data exists

    setLoading(true);
    try {
      const endpoint = isSplit
        ? "https://your-api.com/api/workouts/split/"
        : "https://your-api.com/api/workouts/day/";

      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      const normalizedData = Array.isArray(data) ? data : [data];

      console.log("✅ Fetched Workouts:", normalizedData);
      setGeneratedWorkouts(normalizedData);
      sessionStorage.setItem(
        "generatedWorkouts",
        JSON.stringify(normalizedData)
      );
    } catch (error) {
      console.error("❌ Error fetching workouts:", error);
    }
    setLoading(false);
  };

  // Load workouts if missing
  useEffect(() => {
    if (generatedWorkouts.length === 0) {
      console.warn("⚠️ No workout data found, fetching new data.");
      fetchWorkouts();
    }
  }, []);

  // Reload workouts when user clicks "Generate New Workout"
  const handleReloadWorkout = () => {
    sessionStorage.removeItem("generatedWorkouts"); // Clear cache
    fetchWorkouts();
  };

  // Save Workout Handler
  const handleSaveWorkout = async () => {
    try {
      const response = await fetch("http://localhost:5001/api/workouts/save/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ workouts: generatedWorkouts }),
      });

      if (response.ok) {
        alert("✅ Workout saved successfully!");
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
            <Spinner animation="border" role="status">
              <span className="visually-hidden">Loading...</span>
            </Spinner>
          </div>
        ) : generatedWorkouts.length > 0 ? (
          isSplit ? (
            generatedWorkouts.map((dayWorkout, index) => {
                if (!dayWorkout || !dayWorkout.workout_data) {
                    console.error(`❌ Invalid workout data for day ${index + 1}:`, dayWorkout);
                    return null; // Prevents crashing
                }
            
                const workoutType = dayWorkout.type 
                    ? dayWorkout.type.charAt(0).toUpperCase() + dayWorkout.type.slice(1)
                    : `Workout ${index + 1}`;
            
                return (
                    <div key={index} className="mb-4">
                        <h3 className="text-center">
                            Day {index + 1} - {workoutType}
                        </h3>
                        <WorkoutTable 
                            exercises={dayWorkout.workout_data.map(exercise => ({
                                name: exercise.Exercise,
                                sets: exercise.Sets,
                                reps: exercise.Reps
                            }))} 
                        />
                    </div>
                );
            })
          ) : (
            <WorkoutTable
              exercises={
                generatedWorkouts[0]?.workout_data?.map((exercise) => ({
                  name: exercise.Exercise,
                  sets: exercise.Sets,
                  reps: exercise.Reps,
                })) || []
              }
            />
          )
        ) : (
          <Alert variant="danger" className="text-center">
            No workout data available.
          </Alert>
        )}

        {/* Buttons Section */}
        <div className="text-center mt-4">
          <Button
            variant="primary"
            className="me-3"
            onClick={handleReloadWorkout}
            disabled={loading}
          >
            🔄 Generate New Workout
          </Button>
          <Button
            variant="success"
            onClick={handleSaveWorkout}
            disabled={loading}
          >
            💾 Save My Workout
          </Button>
        </div>
      </Container>
    </Layout>
  );
}

export default ViewGeneratedWorkouts;
