import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import IndexPage from "./pages/IndexPage";
import LiftBot from "./pages/LiftBot";
import Login from "./pages/forms/Login";
import Logout from "./pages/forms/Logout";
import CreateAccount from "./pages/forms/CreateAccount";
import ChangePassword from "./pages/forms/ChangePassword";
import UserInformationForm from "./pages/forms/UserInformationForm";
import GenerateWorkouts from "./pages/workouts/GenerateWorkouts";
import SavedWorkouts from "./pages/workouts/SavedWorkouts";
import ViewGeneratedWorkouts from "./pages/workouts/ViewGeneratedWorkouts";
import MuscleMissionsLogo from "./assets/Muscle_Missions_Logo.png";
import useAuth from "./hooks/useAuth";

function App() {
  const isAuthenticated = useAuth();

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
          element={isAuthenticated ? <Navigate to="/" /> : <Login />}
        />
        <Route
          path="/accounts/create/"
          element={isAuthenticated ? <Navigate to="/" /> : <CreateAccount />}
        />
        <Route
          path="/accounts/edit/"
          element={
            isAuthenticated ? (
              <ChangePassword />
            ) : (
              <Navigate to="/accounts/login/" />
            )
          }
        />
        <Route
          path="/accounts/edit_more_info/"
          element={
            isAuthenticated ? (
              <UserInformationForm />
            ) : (
              <Navigate to="/accounts/login/" />
            )
          }
        />
        <Route path="/accounts/logout/" element={<Logout />} />

        <Route path="/liftbot/" element={<LiftBot />} />
        <Route path="/generated-workout/" element={<ViewGeneratedWorkouts />} />
      </Routes>
    </Router>
  );
}

export default App;
