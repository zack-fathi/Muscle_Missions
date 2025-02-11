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
from muscle.api.daily_workout import generate_daily_workout
from muscle.api.workout_split import generate_workout_split


@muscle.app.route('/workouts/day/')
def show_daily_workout():
    """Show the daily workout page."""

    background_check = utils.do_background_check()
    if background_check:
        return background_check

    return flask.render_template("day.html")


@muscle.app.route('/workouts/split/')
def show_split():
    """Show the workout split page."""
    # if not utils.check_logname_exists():
    #     return flask.redirect("/accounts/login/", 302)
    
    # # check if user hasn't inputted new information
    # if utils.check_user_settings()['age'] == -1:
    #     return flask.redirect("/accounts/more_info/", 302)
    
    background_check = utils.do_background_check()
    if background_check:
        return background_check

    return flask.render_template("split.html")


@muscle.app.route('/workouts/', methods=['POST'])
def handle_workouts_submit():
    """Handle the form submission for creating a workout."""

    # if not utils.check_logname_exists():
    #     return flask.redirect("/accounts/login/", 302)
    
    # # check if user hasn't inputted new information
    # if utils.check_user_settings()['age'] == -1:
    #     return flask.redirect("/accounts/more_info/", 302)

    background_check = utils.do_background_check()
    if background_check:
        return background_check

    connection = muscle.model.get_db()
    form = flask.request.form
    operation = form.get('operation')

    if operation == "daily_workout_generator":
        return daily_workout_help(connection, form)
    if operation == "split_generator":
        return split_help(connection, form)
    
    return None

@muscle.app.route('/save_workout/', methods=['POST'])
def save_workout():
    "Save a users workout."
    # if not utils.check_logname_exists():
    #     return flask.redirect("/accounts/login/", 302)
    
    # # check if user hasn't inputted new information
    # if utils.check_user_settings()['age'] == -1:
    #     return flask.redirect("/accounts/more_info/", 302)
    background_check = utils.do_background_check()
    if background_check:
        return background_check
    
    workout_json = flask.request.form['workout_data']
    workout_data = json.loads(workout_json)
    connection = muscle.model.get_db()
    operation = flask.request.form['operation']
    difficulty = flask.request.form['difficulty']
    time = flask.request.form['time']

    if operation == "save_day":
        save_single_workout(workout_data,time, difficulty)
    elif operation == "save_split":
        user_id = utils.get_user_id(connection)
        save_workout_split(user_id, workout_data, time, difficulty)

    # Redirecting to the index page after saving
    # flask.flash("Your workout has been saved!", "success")
    return flask.redirect("/", 302)

def daily_workout_help(connection, form):
    """Help make the custom daily workout."""

    workout_type = form.get('workout_type')
    muscle_split = form.get('muscle_split')
    equipment = form.getlist('equipment')
    limitations = form.getlist('limitations')
    time = form['time']
    difficulty = utils.get_difficulty(connection)

    workout_data = generate_daily_workout(
        time, equipment, muscle_split, workout_type, difficulty, connection, limitations).json
    workout_json = json.dumps(workout_data, indent=2)

    return flask.render_template("show_workout.html", workout_data=workout_data, workout_json=workout_json, time=time, difficulty=difficulty)


def split_help(connection, form):
    """Help make the custom workout split."""

    frequency = int(form.get('frequency'))
    workout_type = form.get('workout_type')
    equipment = form.getlist('equipment')
    limitations = form.getlist('limitations')
    time = form['time']
    difficulty = utils.get_difficulty(connection)

    workout_data = generate_workout_split(
        time, equipment, workout_type, difficulty, connection, limitations, frequency).json
    
    workout_json = json.dumps(workout_data, indent=2)
    return flask.render_template("show_workout_split.html", workout_data=workout_data, workout_json=workout_json, time=time, difficulty=difficulty)


def save_workout_split(user_id, workout_split_data, duration, difficulty):
    """Save a workout split."""
    connection = muscle.model.get_db()

    # insert into split table
    cur = connection.execute(
        "INSERT INTO workout_splits (userID) VALUES (?) ",
        (user_id,)
    )

    split_id = cur.lastrowid

    for workout_number, day_workout in enumerate(workout_split_data['workout_split'], start=1):

        workout_id = insert_workout(
            connection, user_id, day_workout['type'], workout_number, duration, difficulty,split_id
        )

        for order, exercise in enumerate(day_workout['workout_data'], start=1):
            exercise_id = utils.get_exercise_id_by_name(
                exercise['Exercise'])
            sets = exercise['Sets']
            reps = exercise['Reps']
            if exercise_id:
                insert_exercise(connection, workout_id, exercise_id, order, sets, reps)
    
    connection.commit()


def save_single_workout(workout_data, time, difficulty):
    """Save a single workout."""
    connection = muscle.model.get_db()
    user_id = utils.get_user_id(connection)
    if not user_id:
        raise ValueError("User ID not found")

    # Assuming workout_data has structure similar to a single day in workout_split
    workout_type = workout_data['type']
    duration = time

    # Insert workout details
    cur = connection.execute(
        "INSERT INTO workouts (userID, workoutType, duration, difficulty, workout_number) VALUES (?, ?, ?, ?,?)",
        (user_id, workout_type, duration, difficulty, 1)
    )
    workout_id = cur.lastrowid

    # Insert each exercise in the workout
    for exercise_order, exercise in enumerate(workout_data['workout_data'], start=1):
        exercise_name = exercise['Exercise']
        sets = exercise['Sets']
        reps = exercise['Reps']
        # Assuming you have a way to find exerciseID by exercise name
        exercise_id = utils.get_exercise_id_by_name(exercise_name)
        if exercise_id is not None:
            connection.execute(
                "INSERT INTO workout_exercises (workoutID, exerciseID, orderInWorkout, sets, reps) VALUES (?, ?, ?, ?, ?)",
                (workout_id, exercise_id, exercise_order, sets, reps)
            )

    connection.commit()  # Commit the transaction


def insert_workout(connection, user_id, workout_type, workout_number, duration, difficulty, split_id):
    """Insert into workouts table."""
    
    cur = connection.execute(
        "INSERT INTO workouts (userID, workoutType, workout_number, duration, difficulty, splitID) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, workout_type, workout_number, duration, difficulty, split_id)
    )
    workout_id = cur.lastrowid
    return workout_id



def insert_exercise(connection, workout_id, exercise_id, order_in_workout, sets, reps):
    """Insert into workout_exercises table."""

    connection.execute(
        "INSERT INTO workout_exercises (workoutID, exerciseID, orderInWorkout, sets, reps) VALUES (?, ?, ?, ?, ?)",
        (workout_id, exercise_id, order_in_workout, sets, reps)
    )
    connection.commit()
