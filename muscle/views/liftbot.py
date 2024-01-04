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
        return flask.redirect("/accounts/login/",302)
    
    # TODO: ACCOUNT FOR NULL DATA(WHEN FORM HAS NOT BEEN FILLED OUT)
    user = utils.get_user_information()
    kind_of_workout, user_workout = get_user_workout(user['userID'])
    
    if kind_of_workout == "split":
        formatted_workout = format_workout_split(user_workout)
    else:
        formatted_workout = format_single_workout(user_workout)
    

    # formatted_workout = format_workout(user_workout)
    # Initialize LiftBot session with user profile
    initial_message = {
        "role": "system",
        "content": f"The user's username is {user['username']} and they are a {user['age']} year old {user['gender']}. The user is {user['height']} inches tall and {user['weight']} pounds. They are {utils.activity_map[user['fitness_level']]} and are an {utils.workout_experience_map[user['workout_experience']]} lifter in the gym. Their previous workout/workout split was: {formatted_workout}. Please offer specific tips for each exercise in the workout split, including customization options for different equipment availability. Additionally, provide motivation and recovery advice tailored to the user's profile."
    }

    # completion = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    # messages=[
    #     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    #     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    # ]
    # )

    # print(completion.choices[0].message)

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
            workout =  utils.get_last_split_workout(connection, recent_workout["splitID"])
            return ("split", workout)
        
        workout = utils.get_last_single_workout(connection, recent_workout["workoutID"])
        return("single workout", workout)

    return "There is no recent workout available"

def format_workout_split(workout_data):
    """Format a workout into a readable prompt."""
    formatted_workouts = []
    for day, exercises in enumerate(workout_data, start=1):
        day_workout = f"Day {day}: " + ", ".join([f"{exercise['name']} ({exercise['reps']} reps, {exercise['sets']} sets)" for exercise in exercises])
        formatted_workouts.append(day_workout)
    return " | ".join(formatted_workouts)

def format_single_workout(exercises):
    """Format a single workout."""
    
    return  ", ".join([f"{exercise['name']} ({exercise['reps']} reps, {exercise['sets']} sets)" for exercise in exercises])
