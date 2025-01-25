import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import IndexPage from "./pages/IndexPage";
import YourWorkout from "./pages/YourWorkout";
import WorkoutSplit from "./pages/WorkoutSplit";
import DailyWorkout from "./pages/DailyWorkout";



function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<IndexPage />} />
        <Route path="/your_workout/" element={<YourWorkout />} />
        <Route path="/workout_split/" element={<WorkoutSplit />} />
        <Route path="/daily_workout" element={<DailyWorkout />} />

      </Routes>
    </Router>
  );
}

export default App;