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

    background_check = utils.do_background_check()
    if background_check:
        return background_check
    
    user_id = utils.get_user_id(connection)

    recent_workout = connection.execute(
        "SELECT * FROM workouts WHERE userID = ? ORDER BY workoutID DESC LIMIT 1 ",
        (user_id,)
    ).fetchone()

    workout_data = {}
    if recent_workout:
        if recent_workout["splitID"]:
            workout_data['workout_split'] = utils.get_last_split_workout(connection, recent_workout['splitID'])
            return flask.render_template("saved_workout_split.html", workout_data=workout_data)
        else:
            workout_data['exercises'] = utils.get_last_single_workout(connection, recent_workout['workoutID'])
            return flask.render_template("saved_daily_workout.html", workout_data=workout_data)

    return flask.render_template("saved_daily_workout.html", workout_data=workout_data)
