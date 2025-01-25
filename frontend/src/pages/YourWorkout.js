import React, { useState, useEffect } from "react";
import { Container, Alert } from "react-bootstrap";
import WorkoutTable from "../components/WorkoutTable";
import Layout from "../components/Layout";

function YourWorkout() {
  const [workoutData, setWorkoutData] = useState(null);

  useEffect(() => {
    const fetchWorkoutData = async () => {
      const data = {
        exercises: [
          { name: "Push-Ups", sets: 3, reps: 15 },
          { name: "Squats", sets: 4, reps: 12 },
        ],
      };
      setWorkoutData(data);
    };

    fetchWorkoutData();
  }, []);

  return (
    <Layout>
        <Container className="mt-4">
        <h2 className="text-center mb-4">
            Here is your previously saved Muscle Missions Workout!
        </h2>
        {workoutData && workoutData.exercises.length > 0 ? (
            <WorkoutTable exercises={workoutData.exercises} />
        ) : (
            <Alert variant="danger" className="text-center">
            No workout data available.
            </Alert>
        )}
        </Container>
    </Layout>
  );
}

export default YourWorkout;