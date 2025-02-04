"""Liftbot Service API."""

from flask import jsonify, session
import json
from openai import OpenAI
from dotenv import load_dotenv
from model import get_db
from utils import (
    do_background_check,
    get_user_information,
    get_last_split_workout,
    get_last_single_workout
)

load_dotenv()

client = OpenAI()


def show_liftbot():
    """Retrieve LiftBot screen data."""
    background_check = do_background_check()
    if background_check:
        return jsonify({"error": "Unauthorized"}), 401

    user = get_user_information()
    if not user:
        return jsonify({"error": "User not found"}), 404

    workout_info = get_user_workout(user["userID"])
    prev_workout = workout_info is not None

    initial_message_content = {
        "username": user["username"],
        "age": user["age"],
        "gender": user["gender"],
        "height": user["height"],
        "weight": user["weight"],
        "fitness_level": activity_map[user["fitness_level"]],
        "workout_experience": workout_experience_map[user["workout_experience"]],
    }

    if prev_workout:
        kind_of_workout, user_workout = workout_info
        formatted_workout = (
            format_workout_split(user_workout) if kind_of_workout == "split" else format_single_workout(user_workout)
        )
        initial_message_content["previous_workout"] = formatted_workout
    else:
        initial_message_content["message"] = (
            "It seems you do not have a saved workout. LiftBot works best with workout history."
        )

    session["chat_history"] = [{"role": "system", "content": json.dumps(initial_message_content)}]

    return jsonify(initial_message_content)


def get_user_workout(user_id):
    """Get the user's last workout for prompting."""
    connection = get_db()
    recent_workout = connection.execute(
        "SELECT * FROM workouts WHERE userID = ? ORDER BY workoutID DESC LIMIT 1",
        (user_id,)
    ).fetchone()

    if recent_workout:
        if recent_workout["splitID"]:
            return "split", get_last_split_workout(connection, recent_workout["splitID"])
        return "single workout", get_last_single_workout(connection, recent_workout["workoutID"])

    return None


def format_workout_split(workout_data):
    """Format a workout into a structured JSON response."""
    return [
        {
            "day": day + 1,
            "exercises": [
                {"name": exercise["name"], "reps": exercise["reps"], "sets": exercise["sets"]}
                for exercise in exercises
            ],
        }
        for day, exercises in enumerate(workout_data)
    ]


def format_single_workout(exercises):
    """Format a single workout into a structured JSON response."""
    return [{"name": exercise["name"], "reps": exercise["reps"], "sets": exercise["sets"]} for exercise in exercises]


def process_message(data):
    """Process a message from the user and return a chatbot response."""
    try:
        user_message = data.get("message", "").strip()
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        session["chat_history"].append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=session["chat_history"]
        )

        liftbot_response = response.choices[0].message.content
        session["chat_history"].append({"role": "system", "content": liftbot_response})

        return jsonify({"response": liftbot_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


activity_map = {

    "na":"sedentary (0-2 hours per week of activity)",
    "la":"lightly active (2-3 hours per week of activity)",
    "ma":"moderately active (3-5 hours per week of activity)",
    "va":"very active (5+ days per week of activity)"
}

workout_experience_map = {
    0: "beginner (0-1 years experience)",
    1: "intermediate (1-3 years experience)",
    2: "advanced (3+ years experience)"
}