"""REST API to generate workout split."""
import flask
import muscle
import json
import random
from .daily_workout import generate_daily_fullbody_workout, generate_daily_lower_workout, generate_daily_pull_workout, generate_daily_push_workout, generate_daily_shoulder_workout, generate_workout, generate_daily_upper_workout


def generate_workout_split(time, equipment, muscle_group, workout_type, difficulty, connection, limitations, frequency):
    """Generate a workout split for the user."""

    if frequency == 2:
        workout_split = generate_two_day_split(time, equipment, workout_type,
                               difficulty, connection, limitations)
        return flask.jsonify({"workout_split" :workout_split})
    
    elif frequency == 3:
        workout_split = generate_three_day_split(time, equipment, workout_type,
                               difficulty, connection, limitations)
        return flask.jsonify({"workout_split" :workout_split})
    
    elif frequency == 4:
        workout_split = generate_four_day_split(time, equipment, workout_type,
                               difficulty, connection, limitations)
        return flask.jsonify({"workout_split" :workout_split})

    elif frequency == 5:
        workout_split = generate_five_day_split(time, equipment, workout_type,
                               difficulty, connection, limitations)
        return flask.jsonify({"workout_split" :workout_split})

    elif frequency == 6:
        workout_split = generate_six_day_split(time, equipment, workout_type,
                               difficulty, connection, limitations)
        return flask.jsonify({"workout_split" :workout_split})

    return None


def generate_two_day_split(time, equipment, workout_type, difficulty, connection, limitations):
    """Generate a two day split for the user."""

    # Full Body workout to generate
    workout_split = []

    for _ in range(2):
        daily_workout = generate_daily_fullbody_workout(
            time, equipment, workout_type, difficulty, connection, limitations)
        workout_split.append(daily_workout)

    return workout_split

def generate_three_day_split(time, equipment, workout_type, difficulty, connection, limitations):
    """Generate a three day split for the user."""

    # Full Body workout to generate
    workout_split = []

    for _ in range(3):
        daily_workout = generate_daily_fullbody_workout(
            time, equipment, workout_type, difficulty, connection, limitations)
        workout_split.append(daily_workout)

    return workout_split

def generate_four_day_split(time, equipment, workout_type, difficulty, connection, limitations):
    """Generate a four day split for the user."""

    # Full Body workout to generate
    workout_split = []

    for i in range(4):
        if i % 2 == 0:
            daily_workout = generate_daily_upper_workout(
            time, equipment, workout_type, difficulty, connection, limitations)
        else:
            daily_workout = generate_daily_lower_workout(
            time, equipment, workout_type, difficulty, connection, limitations)
        
        workout_split.append(daily_workout)

    return workout_split

def generate_five_day_split(time, equipment, workout_type, difficulty, connection, limitations):
    """Generate a five day split for the user."""

    # Full Body workout to generate
    workout_split = []

    for i in range(4):
        if i % 2 == 0:
            daily_workout = generate_daily_upper_workout(
            time, equipment, workout_type, difficulty, connection, limitations)
        else:
            daily_workout = generate_daily_lower_workout(
            time, equipment, workout_type, difficulty, connection, limitations)
        
        workout_split.append(daily_workout)
    
    workout_split.append(generate_daily_shoulder_workout(time, equipment, workout_type, difficulty, connection, limitations))

    return workout_split

def generate_six_day_split(time, equipment, workout_type, difficulty, connection, limitations):
    """Generate a six day split for the user."""

    # Full Body workout to generate
    workout_split = []

    for i in range(6):
        if i % 3 == 0:
            daily_workout = generate_daily_push_workout(
            time, equipment, workout_type, difficulty, connection, limitations)
        elif i % 3 == 1:
            daily_workout = generate_daily_pull_workout(
            time, equipment, workout_type, difficulty, connection, limitations)
        else:
            daily_workout = generate_daily_lower_workout(
            time, equipment, workout_type, difficulty, connection, limitations)
        
        workout_split.append(daily_workout)
    
    return workout_split
