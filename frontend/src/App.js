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
import GenerateWorkouts from "./pages/workouts/GenerateWorkouts";
import SavedWorkouts from "./pages/workouts/SavedWorkouts";
import ViewGeneratedWorkouts from "./pages/workouts/ViewGeneratedWorkouts";
import useAuth from "./hooks/useAuth";
import MuscleMissionsLogo from "./assets/Muscle_Missions_Logo.png";
import MyProfile from "./pages/forms/MyProfile";

function App() {
  const { authenticated, loading } = useAuth();

  // Prevent incorrect redirects while auth is still loading
  if (loading) {
    return <div>Loading...</div>;
  }

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
          element={authenticated ? <Navigate to="/" /> : <Login logoSrc={MuscleMissionsLogo} />}
        />
        <Route
          path="/accounts/create/"
          element={authenticated ? <Navigate to="/" /> : <CreateAccount logoSrc={MuscleMissionsLogo} />}
        />
        <Route
          path="/accounts/edit/"
          element={
            authenticated ? <ChangePassword logoSrc={MuscleMissionsLogo} /> : <Navigate to="/accounts/login/" />
          }
        />
        <Route
          path="/accounts/profile/"
          element={
            authenticated ? <MyProfile logoSrc={MuscleMissionsLogo} /> : <Navigate to="/accounts/login/" />
          }
        />
        <Route
          path="/accounts/edit_password/"
          element={
            authenticated ? <ChangePassword logoSrc={MuscleMissionsLogo} /> : <Navigate to="/accounts/login/" />
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
