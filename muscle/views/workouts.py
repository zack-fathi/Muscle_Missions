"""Workouts page."""

import os
import uuid
import hashlib
import pathlib
import flask
import muscle
import requests
import json
from .. import utils
from muscle.api.workout_endpoints import generate_daily_workout

@muscle.app.route('/workouts/day/')
def show_daily_workout():
    """Show the daily workout page."""

    return flask.render_template("day.html")

@muscle.app.route('/workouts/split/')
def show_split():
    """Show the workout split page."""

    return flask.render_template("split.html")

@muscle.app.route('/workouts/', methods = ['POST'])
def handle_workouts_submit():
    """Handle the form submission for creating a workout."""

    connection = muscle.model.get_db()
    form = flask.request.form
    operation = form.get('operation')

    if operation == "daily_workout_generator":
        return daily_workout_help(connection, form)
    if operation == "split_generator":
        return split_help(connection, form)


    return 'HELLO M8 AS YOU CAN SEE I AM NOT DONE WITH THIS YET M8'    
    
def daily_workout_help(connection, form):
    """Help make the custom daily workout."""

    workout_type = form.get('workout_type')
    muscle_split = form.get('muscle_split')
    equipment = form.getlist('equipment')
    limitations = form.getlist('limitations')
    print("equipment = ", equipment)
    time = form['time']
    difficulty = get_difficulty(connection)
    
    workout_data = generate_daily_workout(time, equipment, muscle_split, workout_type,difficulty,connection, limitations).json
    # formatted_workout = json.dumps(workout_data, indent=2)
    print(workout_data)
    return flask.render_template("show_workout.html", workout_data = workout_data)

def split_help(connection, form):
    """Help make the custom workout split."""

    frequency = form.get('frequency')
    workout_type = form.get('workout_type')
    muscle_split = form.get('muscle_split')
    equipment = form.getlist('equipment')
    limitations = form.getlist('limitations')
    print("equipment = ", equipment)
    time = form['time']
    difficulty = get_difficulty(connection)
    
    workout_data = generate_daily_workout(time, equipment, muscle_split, workout_type,difficulty,connection, limitations).json
    # formatted_workout = json.dumps(workout_data, indent=2)
    print(workout_data)
    return flask.render_template("show_workout.html", workout_data = workout_data)

    return NotImplemented

def generate_workout(type, group, split):
    """Generate a custom workout for the user."""

    # API call to fetch list of exercises 
    querystring = {"time":"30","equipment":"dumbbells","muscle":"biceps","fitness_level":"beginner","fitness_goals":"strength"}


    response = requests.get(muscle.config.WORKOUT_PLANNER_API_URL, headers=muscle.config.WORKOUT_PLANNER_HEADERS, params=querystring)

    return response.json()


def get_difficulty(connection):
    """Get a user's difficulty."""

    logname = flask.request.cookies.get('username')

    cur = connection.execute(
        "SELECT workout_experience "
        "FROM users "
        "WHERE username == ?",
        (logname,)
    )

    return cur.fetchone()['workout_experience']
