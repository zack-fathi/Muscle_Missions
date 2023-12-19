"""Config file."""
import pathlib

APPLICATION_ROOT = '/'

# File Upload to var/uploads/
ROOT = pathlib.Path(__file__).resolve().parent.parent

DATABASE_FILENAME = ROOT/'var'/'muscle.sqlite3'

EXERCISES_API_URL = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"

EXERCISES_API_HEADERS = {
	"X-RapidAPI-Key": "15cfe84b49msh04b611316f5d356p1e8ad1jsnd68d88ee2879",
	"X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com"
}

WORKOUT_PLANNER_API_URL = "https://workout-planner1.p.rapidapi.com/customized"

WORKOUT_PLANNER_HEADERS = {
	"X-RapidAPI-Key": "15cfe84b49msh04b611316f5d356p1e8ad1jsnd68d88ee2879",
	"X-RapidAPI-Host": "workout-planner1.p.rapidapi.com"
}

EXERCISE_DB_API_URL = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/back"

EXERCISE_DB_API_HEADERS = {
	"X-RapidAPI-Key": "15cfe84b49msh04b611316f5d356p1e8ad1jsnd68d88ee2879",
	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}



