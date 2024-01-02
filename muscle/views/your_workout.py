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
            print("SPLIT ID IS ", recent_workout["splitID"])
            workout_data['workout_split'] = split_workout_viewer(connection, recent_workout['splitID'])
            return flask.render_template("saved_workout_split.html", workout_data=workout_data)
        else:
            workout_data['exercises'] = single_workout_viewer(connection, recent_workout['workoutID'])
            return flask.render_template("saved_daily_workout.html", workout_data=workout_data)

    return workout_data

def split_workout_viewer(connection, split_id):
    """Show the workout split."""

    split_workouts = connection.execute(
        "SELECT * FROM workouts WHERE splitID = ? ",
        (split_id,)
    ).fetchall()

    combined_workout = []
    for workout in split_workouts:
        exercises = connection.execute(
            "SELECT e.name FROM workout_exercises we JOIN exercises e ON we.exerciseID = e.exerciseID WHERE we.workoutID = ? ",
            (workout["workoutID"],)
        ).fetchall()
        combined_workout.append(exercises)

    return combined_workout

def single_workout_viewer(connection, workoutID):
    """Show the workout."""
    workout_exercises = connection.execute(
        "SELECT e.name FROM workout_exercises we JOIN exercises e ON we.exerciseID = e.exerciseID WHERE we.workoutID = ?",
        (workoutID,)
    ).fetchall()
    return workout_exercises