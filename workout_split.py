"""REST API to generate workout split."""
import flask
import muscle
import json
import random
from .. import utils
from .daily_workout import generate_workout

def generate_workout_split(time, equipment, workout_type, difficulty, connection, limitations, frequency):
    """Generate a workout split for the user."""
    background_check = utils.do_background_check()
    if background_check:
        return background_check
    
    workout_split = []
    index = frequency - 2 

    # if frequency < 4:
    #     parent_exercises_dict = {}

    for muscle_group in utils.workout_split_order[index]:
        group_order = utils.get_dynamic_workout_order(time, muscle_group)
        daily_workout = generate_workout(
            group_order, equipment, workout_type, difficulty, connection, limitations,muscle_group)
        workout_split.append(daily_workout)

    return flask.jsonify({"workout_split" :workout_split})
