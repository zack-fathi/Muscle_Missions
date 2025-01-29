import React from "react";
import { Table } from "react-bootstrap";
import "../styles/WorkoutTable.css"; // Ensure correct import

function WorkoutTable({ title, exercises }) {
  return (
    <div className="workout-table-container">
      {title && <h3 className="workout-day-title">{title}</h3>} {/* ✅ Centered */}
      <Table bordered className="workout-table">
        <thead>
          <tr>
            <th scope="col">Exercise</th>
            <th scope="col">Sets</th>
            <th scope="col">Reps</th>
          </tr>
        </thead>
        <tbody>
          {exercises.length > 0 ? (
            exercises.map((exercise, index) => (
              <tr key={index}>
                <td>{exercise.name}</td>
                <td>{exercise.sets}</td>
                <td>{exercise.reps}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="3" className="text-center text-danger">
                No workout data available.
              </td>
            </tr>
          )}
        </tbody>
      </Table>
    </div>
  );
}

export default WorkoutTable;
