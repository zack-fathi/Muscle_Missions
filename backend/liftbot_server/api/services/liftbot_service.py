"""Liftbot Service API."""

from flask import jsonify, session
import json
from openai import OpenAI
from dotenv import load_dotenv
import os
from model import get_db
from utils import (
    do_background_check,
    get_user_information,
    get_last_split_workout,
    get_last_single_workout,
    get_last_saved_workout
)

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def init_liftbot():
    """Retrieve LiftBot screen data."""
    background_check = do_background_check()
    if background_check:
        return jsonify({"error": "Unauthorized"}), 401

    user = get_user_information()
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Extract JSON data correctly
    workout_response = get_last_saved_workout()

    if isinstance(workout_response, tuple):  # Handle (data, status_code)
        workout_response = workout_response[0]

    if isinstance(workout_response, dict):  # Ensure it's a dictionary
        workout_info = workout_response
    else:
        workout_info = None  # Default to None if invalid

    prev_workout = workout_info is not None

    initial_message_content = {
        "username": user["username"],
        "workout_experience": workout_experience_map[user["workout_experience"]],
    }

    # Store workout in session but do not send it in the response
    session["workout_info"] = workout_response if prev_workout else {}
    session.modified = True

    initial_message_content["message"] = "Hello! How can I assist with your fitness journey today?"

    # Initialize chat history properly
    if "chat_history" not in session:
        session["chat_history"] = []

    session["chat_history"].append({"role": "system", "content": json.dumps(initial_message_content)})
    session.modified = True  
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
        print(user_message)
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        # Retrieve stored workout data from session
        workout_info = session.get("workout_info", {})
        print("Response from session:", workout_info)

        # Ensure chat history is initialized
        if "chat_history" not in session:
            session["chat_history"] = []

        # Append user message
        session["chat_history"].append({"role": "user", "content": user_message})
        session.modified = True  

        # if workout data exists, add it to chat history context
        if workout_info:
            session["chat_history"].append({"role": "system", "content": json.dumps({"workout_info": workout_info})})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=session["chat_history"]
        )

        liftbot_response = response.choices[0].message.content
        session["chat_history"].append({"role": "system", "content": liftbot_response})
        session.modified = True  

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