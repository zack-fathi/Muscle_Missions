import React, { useState, useEffect } from "react";
import { Container, Alert, Spinner } from "react-bootstrap";
import WorkoutTable from "../../components/WorkoutTable";
import Layout from "../../components/Layout";
import "../../styles/WorkoutTable.css";
import { Helmet } from "react-helmet";

const authURL = process.env.REACT_APP_AUTH_URL;
const workoutsURL = process.env.REACT_APP_WORKOUTS_URL;

function SavedWorkouts() {
  const [workoutData, setWorkoutData] = useState(null);
  const [isSplit, setIsSplit] = useState(false);
  const [loading, setLoading] = useState(true);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    async function doCheck() {
      try {
        const res = await fetch(`${authURL}/auth/`, {
          credentials: "include",
        });
        if (res.ok) {
          const data = await res.json();
          setIsLoggedIn(data.logged_in);
          if (data.logged_in) {
            // fetch last saved workout
            fetchLastSavedWorkout();
          } else {
            setLoading(false);
          }
        } else {
          setIsLoggedIn(false);
          setLoading(false);
        }
      } catch (error) {
        setIsLoggedIn(false);
        setLoading(false);
      }
    }
  
    doCheck();
  }, []);
  
  const fetchLastSavedWorkout = async () => {
    try {
      const response = await fetch(`${workoutsURL}/last_saved/`, {
        method: "GET",
        credentials: "include", // send cookies
      });

      if (!response.ok) {
        console.error(`❌ API Error: ${response.status} - ${response.statusText}`);
        return;
      }

      const data = await response.json();
      console.log("✅ Raw Workout Data:", data);

      // Expecting shape: { days: [ { type, workout_data }, { ... } ] }
      if (data.days && Array.isArray(data.days)) {
        setWorkoutData(data);
        setIsSplit(data.days.length > 1);
      } else {
        // If the shape doesn't match, set no data
        setWorkoutData(null);
      }

    } catch (error) {
      console.error("❌ Error fetching last saved workout:", error);
      setWorkoutData(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <Helmet>
        <title>Your Saved Workout</title>
      </Helmet>
      <Container className="mt-4">
        <h2 className="text-center mb-4 workout-heading">
          {isSplit
            ? "Here is your previously saved Workout Split!"
            : "Here is your previously saved Workout!"}
        </h2>

        {loading ? (
          <div className="text-center">
            <Spinner animation="border" role="status">
              <span className="visually-hidden">Loading...</span>
            </Spinner>
          </div>
        ) : isLoggedIn ? (
          workoutData && workoutData.days ? (
            workoutData.days.map((day, index) => {
              // Capitalize the first letter of day.type
              const displayType = day.type
                ? day.type.charAt(0).toUpperCase() + day.type.slice(1)
                : "Workout";

              return (
                <WorkoutTable
                  key={index}
                  title={
                    workoutData.days.length > 1
                      ? `Day ${index + 1} — ${displayType}`
                      : displayType
                  }
                  exercises={day.workout_data}
                />
              );
            })
          ) : (
            <Alert variant="danger" className="text-center">
              No workout data available.
            </Alert>
          )
        ) : (
          // If user is NOT logged in, show your message
          <Alert variant="danger" className="text-center">
            You must be logged in to see your last saved workout.
          </Alert>
        )}
      </Container>
    </Layout>
  );
}

export default SavedWorkouts;
