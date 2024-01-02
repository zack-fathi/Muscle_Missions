"""Your previous workouts page."""

import os
import uuid
import hashlib
import pathlib
import flask
import muscle
import requests
import json
from .. import utils
from muscle.api.daily_workout import generate_daily_workout
from muscle.api.workout_split import generate_workout_split


@muscle.app.route('/your_workout/')
def show_your_workout():

    connection = muscle.model.get_db()

    if not utils.check_logname_exists():
        return flask.redirect("/accounts/login/", 302)
    
    user_id = utils.get_user_id(connection)

    recent_workout = connection.execute(
        "SELECT * FROM workouts WHERE userID = ? ORDER BY workoutID DESC LIMIT 1 ",
        (user_id,)
    ).fetchone()
    print("RECENT WORKOUT IS, ", recent_workout)

    workout_data = {}
    if recent_workout:
        if recent_workout["splitID"]:
            workout_data['split_workouts'] = split_workout_viewer(connection, recent_workout['splitID'])
            
        else:
            workout_data['exercises'] = single_workout_viewer(connection, recent_workout['workoutID'])
    return workout_data

def split_workout_viewer(connection, split_id):
    """Show the workout split."""

    split_workouts = connection.execute(
        "SELECT * FROM workout_exercises WHERE splitID = ? ",
        (split_id,)
    ).fetchall()
    return split_workouts

def single_workout_viewer(connection, workoutID):
    """Show the workout."""
    workout_exercises = connection.execute(
        "SELECT * FROM workout_exercises WHERE workoutID = ?",
        (workoutID,)
    ).fetchall()
    return workout_exercises