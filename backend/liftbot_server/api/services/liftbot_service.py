"""Liftbot Service API."""

from flask import jsonify, session, request
import json
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)

client = OpenAI(api_key=api_key)


def init_liftbot(request):
    """Retrieve LiftBot screen data."""

    logged_in_user = call_auth_server(request)
    if not logged_in_user:
        return jsonify({"error": "Unauthorized"}), 401

    user = get_user_profile(request)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Extract JSON data correctly
    workout_info = get_last_saved_workout(request)

    prev_workout = workout_info is not None

    initial_message_content = {
        "username": user["username"],
        "workout_experience": workout_experience_map[user["workout_experience"]],
    }

    # Store workout in session but do not send it in the response
    session["workout_info"] = workout_info if prev_workout else {}
    session.modified = True

    initial_message_content["message"] = "Hello! How can I assist with your fitness journey today?"

    # Initialize chat history properly
    if "chat_history" not in session:
        session["chat_history"] = []

    session["chat_history"].append({"role": "system", "content": json.dumps(initial_message_content)})
    session.modified = True  
    return jsonify(initial_message_content)

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

def call_auth_server(req):
    """Call the auth server to retrieve user information."""
    
    auth_url = "http://localhost:5002/api/accounts/auth/"

    # forward cookies 
    cookies = req.cookies

    try:
        response = requests.get(auth_url, cookies=cookies, timeout=5)
        # rely on the flag since all reponses have 200
        auth_data = response.json()
        return auth_data
    except requests.exceptions.RequestException as e:
        print("Error contacting auth server:", e)
        return None
    
def get_user_profile(req):
    """Retrieve the user's profile information. This information does not have to be completed, but it helps the Liftbot."""

    profile_url = "http://localhost:5002/api/accounts/profile/"
    cookies = req.cookies

    try:
        response = requests.get(profile_url, cookies=cookies, timeout=5)
        profile_data = response.json()
        return profile_data
    except requests.exceptions.RequestException as e:
        print("Error getting profile of user:", e)
        return None
    
def get_last_saved_workout(req):
    """Retrieve the last saved workout for the user."""
    workout_url = "http://localhost:5001/api/workouts/last_saved/"
    cookies = req.cookies

    try:
        response = requests.get(workout_url, cookies=cookies, timeout=5)
        workout_data = response.json()
        return workout_data
    except requests.exceptions.RequestException as e:
        print("Error getting last saved workout:", e)
        return None

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