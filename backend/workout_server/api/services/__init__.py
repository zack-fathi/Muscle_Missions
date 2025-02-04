"""Initialize Workout Services."""
from .workouts_service import generate_workout_plan, save_workout, get_last_saved_workout
def register_services():
    """Dynamically register services for workouts."""
    return {
        "workouts": {
            "generate_workout_plan": generate_workout_plan,
            "save_workout": save_workout,
            "get_last_saved_workout": get_last_saved_workout,
        }
    }
