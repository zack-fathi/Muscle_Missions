"""REST API to generate workouts."""
import flask
import muscle
import json
import random
from .. import utils
from enum import Enum

def generate_daily_workout(time, equipment, muscle_group, workout_type, difficulty, connection, limitations):
    """Generate a daily workout for the user."""

    background_check = utils.do_background_check()
    if background_check:
        return background_check
    
    group_order = utils.get_dynamic_workout_order(time,muscle_group)
    return flask.jsonify(generate_workout(group_order, equipment, workout_type, difficulty, connection, limitations,muscle_group))

def generate_workout(group_order, equipment, workout_type, difficulty, connection, limitations, muscle_group):
    """Generate workout based on time and group order."""

    workout_plan = []
    selected_exercises = set()  # Set to keep track of selected exercises
    weight = 5  # This is the weight OF an exercise, NOT weight FOR an exercise 
    count = 0

    for muscle_to_hit in group_order:
        exercise = choose_an_exercise(
            muscle_to_hit[0], muscle_to_hit[1], equipment, workout_type, difficulty, muscle_to_hit[2], connection, selected_exercises, limitations, weight)
        if exercise:  # Only add if an exercise was found and not already selected
            workout_plan.append(exercise)
            # Add the selected exercise to the set
            selected_exercises.add(exercise["Parent Exercise"])
        
        count = count + 1
        if count % 3 == 0 and count != 0:
            weight = weight - 1

    workout = {
        "type": muscle_group,
        "workout_data": workout_plan}
    return workout


def choose_an_exercise(muscle_to_hit, muscle_subgroup, equipment_list, workout_type, workout_experience, is_compound, connection, selected_exercises,limitations, weight):
    """Return one exercise chosen, ensuring no repetitions."""

    workouts_to_pick_from = []

    sql_query = """
    SELECT name, parent_exercise FROM exercises
    WHERE muscle_group == ? 
    AND type == ? 
    AND weight >= ? 
    AND (difficulty == ? OR difficulty == 3)
    AND is_compound == ?
    """

    # Add equipment to the query
    equipment_placeholders = ', '.join('?' * len(equipment_list))
    sql_query += f"AND equipment IN ({equipment_placeholders})"

    # Add main_muscle conditionally
    if muscle_subgroup != "all":
        sql_query += " AND main_muscle == ?"

    # Add limitations conditionally
    limitation_placeholders = ', '.join('?' * len(limitations))
    if limitations:
        sql_query += f" AND movement_type NOT IN ({limitation_placeholders})"

    # Add check for repeats
    placeholders = ', '.join('?' * len(selected_exercises))
    if selected_exercises:
        sql_query += f" AND parent_exercise NOT IN ({placeholders})"

    # Construct the query parameters
    query_params = [muscle_to_hit, workout_type, weight, workout_experience, is_compound] + equipment_list
    if muscle_subgroup != "all":
        query_params.append(muscle_subgroup)
    query_params += limitations + list(selected_exercises)

    # Execute the query
    cur = connection.execute(sql_query, query_params)
    query_result = cur.fetchall()

    if query_result:
        for result in query_result:
            workouts_to_pick_from.append({"Exercise": result['name'],
                                            "Sets": "3",
                                            "Reps": "10",
                                            "Parent Exercise": result['parent_exercise']})


    if workouts_to_pick_from:
        return random.choice(workouts_to_pick_from)
    else:
        return None
