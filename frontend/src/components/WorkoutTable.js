import React from "react";
import { Table } from "react-bootstrap";

function WorkoutTable({ exercises, title }) {
  return (
    <div className="mb-4">
      {title && <h3 className="text-center mb-3">{title}</h3>}
      <Table bordered hover>
        <thead className="thead-dark">
          <tr>
            <th>Exercise</th>
            <th>Sets</th>
            <th>Reps</th>
          </tr>
        </thead>
        <tbody>
          {exercises.map((exercise, index) => (
            <tr key={index}>
              <td>{exercise.name}</td>
              <td>{exercise.sets}</td>
              <td>{exercise.reps}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default WorkoutTable;