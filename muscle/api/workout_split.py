"""REST API to generate workout split."""
import flask
import muscle
import json
import random
from ..utils import check_logname_exists, get_dynamic_workout_order, workout_split_order
from .daily_workout import generate_workout

def generate_workout_split(time, equipment, workout_type, difficulty, connection, limitations, frequency):
    """Generate a workout split for the user."""
    if not check_logname_exists():
        return flask.redirect("/accounts/login/", 302)
    
    workout_split = []
    index = frequency - 2 

    # if frequency < 4:
    #     parent_exercises_dict = {}

    for muscle_group in workout_split_order[index]:
        group_order = get_dynamic_workout_order(time, muscle_group)
        daily_workout = generate_workout(
            group_order, equipment, workout_type, difficulty, connection, limitations,muscle_group)
        workout_split.append(daily_workout)

    return flask.jsonify({"workout_split" :workout_split})
