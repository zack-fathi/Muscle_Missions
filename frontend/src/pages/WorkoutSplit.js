import React from "react";
import { Container, Alert } from "react-bootstrap";
import WorkoutTable from "../components/WorkoutTable";

function WorkoutSplit({ workoutData }) {
    
  return (
    <Container className="mt-4">
      <h2 className="mb-4 text-center">
        Here is your previously saved Muscle Missions Workout Split!
      </h2>

      {workoutData && workoutData.workout_split && workoutData.workout_split.length > 0 ? (
        workoutData.workout_split.map((day, dayIndex) => (
          <WorkoutTable
            key={dayIndex}
            title={`Day ${dayIndex + 1}`}
            exercises={day}
          />
        ))
      ) : (
        <Alert variant="danger" className="text-center">
          No workout split data available.
        </Alert>
      )}
    </Container>
  );
}

export default WorkoutSplit;