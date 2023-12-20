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
    form = flask.request.form.to_dict()
    operation = form['operation']

    if operation == "daily_workout_generator":
        return daily_workout_help(connection, form)
    if operation == "split_generator":
        return split_help(connection, form)


    return 'HELLO M8 AS YOU CAN SEE I AM NOT DONE WITH THIS YET M8'    
    
def daily_workout_help(connection, form):
    """Help make the custom daily workout."""

    workout_type = form['workout_type']
    muscle_split = form['muscle_split']
    equipment = form['equipment']
    time = form['time']

    equipment_string = ','.join(equipment)

    # MAKE THE API CALL HERE

def split_help(connection, form):
    """Help make the custom workout split."""

    return NotImplemented

def generate_workout(type, group, split):
    """Generate a custom workout for the user."""

    # API call to fetch list of exercises 
    querystring = {"time":"30","equipment":"dumbbells","muscle":"biceps","fitness_level":"beginner","fitness_goals":"strength"}


    response = requests.get(muscle.config.WORKOUT_PLANNER_API_URL, headers=muscle.config.WORKOUT_PLANNER_HEADERS, params=querystring)

    return response.json()

