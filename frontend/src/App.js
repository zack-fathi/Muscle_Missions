import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import IndexPage from "./pages/IndexPage";
import LiftBot from "./pages/LiftBot";
import Login from "./pages/forms/Login";
import CreateAccount from "./pages/forms/CreateAccount";
import ChangePassword from "./pages/forms/ChangePassword";
import UserInformationForm from "./pages/forms/UserInformationForm";
import GenerateWorkouts from "./pages/workouts/GenerateWorkouts";
import SavedWorkouts from "./pages/workouts/SavedWorkouts";
import ViewGeneratedWorkouts from "./pages/workouts/ViewGeneratedWorkouts";
import MuscleMissionsLogo from "./assets/Muscle_Missions_Logo.png"; 


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<IndexPage />} />
        <Route
          path="/workouts/day/"
          element={
            <GenerateWorkouts
              title="Create Your Daily Workout"
              showDaysPerWeek={false}
            />
          }
        />
        <Route path="/saved_workouts/" element={<SavedWorkouts />} />
        <Route
          path="/workouts/split/"
          element={
            <GenerateWorkouts
              title="Create Your Workout Split"
              showDaysPerWeek={true}
            />
          }
        />
        <Route
          path="/accounts/login/"
          element={<Login logoSrc={MuscleMissionsLogo} />}
        />
        <Route
          path="/accounts/create/"
          element={<CreateAccount logoSrc={MuscleMissionsLogo} />}
        />
        <Route
          path="/accounts/edit/"
          element={
            <ChangePassword logoSrc={MuscleMissionsLogo} />
          }
        />
        <Route
          path="/accounts/edit_more_info/"
          element={
            <UserInformationForm logoSrc={MuscleMissionsLogo} />
          }
        />
        <Route path="/liftbot/" element={<LiftBot />} />
        <Route path="/generated-workout/" element={<ViewGeneratedWorkouts />} />
      </Routes>
    </Router>
  );
}

export default App;
