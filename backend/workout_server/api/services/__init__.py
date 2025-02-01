"""Initialize Workout Services."""
from .workouts_service import generate_workout_plan
def register_services():
    """Dynamically register services for workouts."""
    return {
        "workouts": {
            "generate_workout_plan": generate_workout_plan,
        }
    }
