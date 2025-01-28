import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import IndexPage from "./pages/IndexPage";
import YourWorkout from "./pages/YourWorkout";
import WorkoutSplit from "./pages/WorkoutSplit";
import LiftBot from "./pages/LiftBot";
import Login from "./pages/Login";
import CreateAccount from "./pages/CreateAccount";
import ChangePassword from "./pages/ChangePassword";
import UserInformationForm from "./pages/UserInformationForm";
import WorkoutPage from "./pages/WorkoutPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<IndexPage />} />
        <Route path="/your_workout/" element={<YourWorkout />} />
        <Route path="/workout_split/" element={<WorkoutSplit />} />
        <Route
          path="/workouts/day/"
          element={
            <WorkoutPage
              title="Create Your Daily Workout"
              showDaysPerWeek={false}
            />
          }
        />
        <Route
          path="/workouts/split/"
          element={
            <WorkoutPage
              title="Create Your Workout Split"
              showDaysPerWeek={true}
            />
          }
        />
        <Route
          path="/accounts/login/"
          element={<Login logoSrc="/images/Muscle_Missions_Logo.png" />}
        />
        <Route
          path="/accounts/create/"
          element={<CreateAccount logoSrc="/images/Muscle_Missions_Logo.png" />}
        />
        <Route
          path="/accounts/edit/"
          element={
            <ChangePassword logoSrc="/images/Muscle_Missions_Logo.png" />
          }
        />
        <Route
          path="/accounts/edit_more_info/"
          element={
            <UserInformationForm logoSrc="/images/Muscle_Missions_Logo.png" />
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
