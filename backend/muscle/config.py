"""Config file."""
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Config class."""
    APPLICATION_ROOT = os.getenv('APPLICATION_ROOT', '/')
    ROOT = Path(__file__).resolve().parent.parent
    DATABASE_FILENAME = ROOT / os.getenv('DATABASE_RELATIVE_PATH', 'var/muscle.sqlite3')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    EXERCISES_API_URL = os.getenv('EXERCISES_API_URL', 'default-exercises-api-url')
    EXERCISES_API_KEY = os.getenv('EXERCISES_API_KEY', 'default-exercises-api-key')
    WORKOUT_PLANNER_API_URL = os.getenv('WORKOUT_PLANNER_API_URL', 'default-workout-planner-api-url')
    WORKOUT_PLANNER_API_KEY = os.getenv('WORKOUT_PLANNER_API_KEY', 'default-workout-planner-api-key')
    EXERCISE_DB_API_URL = os.getenv('EXERCISE_DB_API_URL', 'default-exercise-db-api-url')
    EXERCISE_DB_API_KEY = os.getenv('EXERCISE_DB_API_KEY', 'default-exercise-db-api-key')
