"""Your previous workouts page."""

import os
import uuid
import hashlib
import pathlib
import flask
from openai import OpenAI
import muscle
import requests
import json
from .. import utils


client = OpenAI()


@muscle.app.route("/liftbot/")
def show_liftbot():
    """Show the liftbot screen."""

    if not utils.check_logname_exists():
        return flask.redirect("/accounts/login/", 302)

    user = utils.get_user_information()
    kind_of_workout, user_workout = get_user_workout(user['userID'])

    formatted_workout = format_workout(user_workout, kind_of_workout)

    initial_message_content = f"The user's username is {user['username']} and they are a {user['age']} year old {user['gender']}. The user is {user['height']} inches tall and {user['weight']} pounds. They are {utils.activity_map[user['fitness_level']]} and are an {utils.workout_experience_map[user['workout_experience']]} lifter in the gym. Their previous workout/workout split was: {formatted_workout}. Please offer specific tips for each exercise in the workout split, including customization options for different equipment availability. Additionally, provide motivation and recovery advice tailored to the user's profile."

    flask.session['chat_history'] = [{"role": "system", "content": initial_message_content}]

    return flask.render_template("liftbot.html")


def get_user_workout(user_id):
    """Get the user's last workout for prompting."""

    connection = muscle.model.get_db()
    recent_workout = connection.execute(
        "SELECT * FROM workouts WHERE userID = ? ORDER BY workoutID DESC LIMIT 1 ",
        (user_id,)
    ).fetchone()

    if recent_workout:
        if recent_workout["splitID"]:
            workout = utils.get_last_split_workout(
                connection, recent_workout["splitID"])
            return ("split", workout)

        workout = utils.get_last_single_workout(
            connection, recent_workout["workoutID"])
        return ("single workout", workout)

    return "There is no recent workout available"


def format_workout_split(workout_data):
    """Format a workout into a readable prompt."""
    formatted_workouts = []
    for day, exercises in enumerate(workout_data, start=1):
        day_workout = f"Day {day}: " + ", ".join(
            [f"{exercise['name']} ({exercise['reps']} reps, {exercise['sets']} sets)" for exercise in exercises])
        formatted_workouts.append(day_workout)
    return " | ".join(formatted_workouts)


def format_single_workout(exercises):
    """Format a single workout."""

    return ", ".join([f"{exercise['name']} ({exercise['reps']} reps, {exercise['sets']} sets)" for exercise in exercises])


@muscle.app.route("/process_message/", methods=['POST'])
def process_message():
    """Process a message from the user."""
    try:
        data = flask.request.get_json()
        user_message = data['message']

        # Append the user message to the chat history
        flask.session['chat_history'].append({"role": "user", "content": user_message})

        # Send the updated chat history to OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=flask.session['chat_history']
        )

        # Extract the response text
        liftbot_response = response.choices[0].message
        print(liftbot_response)
        # Append the bot response to the chat history
        flask.session['chat_history'].append({"role": "system", "content": liftbot_response})

        # Return a JSON serializable response
        return flask.jsonify({'response': liftbot_response})

    except Exception as e:
        # If an error occurs, return the error message in a serializable format
        return flask.jsonify({'error': str(e)})

