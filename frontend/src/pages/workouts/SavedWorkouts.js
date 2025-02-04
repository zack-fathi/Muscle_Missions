import React, { useState, useEffect } from "react";
import { Container, Alert } from "react-bootstrap";
import WorkoutTable from "../../components/WorkoutTable";
import Layout from "../../components/Layout";
import "../../styles/WorkoutTable.css"; // ✅ Import styling

function SavedWorkouts() {
  const [workoutData, setWorkoutData] = useState(null);
  const [isSplit, setIsSplit] = useState(false);

  useEffect(() => {
    const fetchLastSavedWorkout = async () => {
      try {
        const response = await fetch("http://localhost:5001/api/workouts/last_saved/");
        if (response.ok) {
          const data = await response.json();
          setWorkoutData(data);
          setIsSplit(data.workout_split && data.workout_split.length > 0);
        }
      } catch (error) {
        console.error("❌ Error fetching last saved workout:", error);
      }
    };
  
    fetchLastSavedWorkout();
  }, []);
  
  return (
    <Layout>
      <Container className="mt-4">
        <h2 className="text-center mb-4 workout-heading">
          {isSplit
            ? "Here is your previously saved Muscle Missions Workout Split!"
            : "Here is your previously saved Muscle Missions Workout!"}
        </h2>

        {workoutData ? (
          isSplit ? (
            workoutData.workout_split.map((day, index) => (
              <WorkoutTable
                key={index}
                title={`Day ${index + 1}`} // ✅ This will now be centered
                exercises={day}
              />
            ))
          ) : workoutData.exercises && workoutData.exercises.length > 0 ? (
            <WorkoutTable exercises={workoutData.exercises} />
          ) : (
            <Alert variant="danger" className="text-center">
              No workout data available.
            </Alert>
          )
        ) : (
          <Alert variant="info" className="text-center">
            Loading workout data...
          </Alert>
        )}
      </Container>
    </Layout>
  );
}

export default SavedWorkouts;
