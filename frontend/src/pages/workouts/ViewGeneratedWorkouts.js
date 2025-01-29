import React, { useState } from "react";
import { useLocation } from "react-router-dom";
import { Container, Button, Alert, Spinner } from "react-bootstrap";
import Layout from "../../components/Layout";
import WorkoutTable from "../../components/WorkoutTable";

function ViewGeneratedWorkouts() {
  const location = useLocation();
  const formData = location.state?.formData || {}; // Get submitted workout preferences

  // Determine if this is a multi-day split
  const isSplit = formData.frequency && parseInt(formData.frequency) > 1;

  // State to store generated workouts
  const [generatedWorkouts, setGeneratedWorkouts] = useState([]);
  const [loading, setLoading] = useState(false); // Loading state

  // Function to call API to generate workouts
  const fetchWorkouts = async () => {
    setLoading(true);
    try {
      const response = await fetch("https://your-api.com/generate-workout", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData), // Send user preferences
      });

      const data = await response.json();
      setGeneratedWorkouts(data.workouts || []); // Update workouts from API
    } catch (error) {
      console.error("Error fetching workouts:", error);
    }
    setLoading(false);
  };

  // Load workouts on first render
  React.useEffect(() => {
    fetchWorkouts();
  }, []);

  // Reload workouts when user clicks "Generate New Workout"
  const handleReloadWorkout = () => {
    fetchWorkouts();
  };

  // Save Workout Handler (Modify to send to backend)
  const handleSaveWorkout = async () => {
    try {
      const response = await fetch("https://your-api.com/save-workout", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ workouts: generatedWorkouts }),
      });

      if (response.ok) {
        alert("Workout saved successfully!"); // Replace with UI feedback
      } else {
        alert("Failed to save workout.");
      }
    } catch (error) {
      console.error("Error saving workout:", error);
    }
  };

  return (
    <Layout>
      <Container className="mt-4">
        <h2 className="text-center mb-4">
          {isSplit ? "Here is your Multi-Day Workout Split!" : "Here is your Generated Workout!"}
        </h2>

        {loading ? (
          <div className="text-center">
            <Spinner animation="border" role="status">
              <span className="visually-hidden">Loading...</span>
            </Spinner>
          </div>
        ) : generatedWorkouts.length > 0 ? (
          isSplit ? (
            generatedWorkouts.map((dayWorkout, index) => (
              <div key={index} className="mb-4">
                <h3 className="text-center">Day {index + 1}</h3>
                <WorkoutTable exercises={dayWorkout} />
              </div>
            ))
          ) : (
            <WorkoutTable exercises={generatedWorkouts} />
          )
        ) : (
          <Alert variant="danger" className="text-center">
            No workout data available.
          </Alert>
        )}

        {/* Buttons Section */}
        <div className="text-center mt-4">
          <Button variant="primary" className="me-3" onClick={handleReloadWorkout} disabled={loading}>
            🔄 Generate New Workout
          </Button>
          <Button variant="success" onClick={handleSaveWorkout} disabled={loading}>
            💾 Save My Workout
          </Button>
        </div>
      </Container>
    </Layout>
  );
}

export default ViewGeneratedWorkouts;
