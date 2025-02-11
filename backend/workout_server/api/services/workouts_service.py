"""Workout Service - Handles workout generation and retrieval."""

import json
import random
from flask import jsonify
from model import get_db
from utils import get_dynamic_workout_order
import requests

def generate_workout_plan(data, is_split=False):
    """Generate a daily workout or a workout split based on input parameters."""

    print("data: ", data)

    # Extract fields from frontend form
    time = data["time"]
    equipment = data.get("equipment", [])
    difficulty = data["difficulty"]
    limitations = data.get("limitations", [])

    connection = get_db()

    if is_split:
        # Multi-day split workout generation
        frequency = int(data["frequency"])
        workout_plan = []
        index = frequency - 2  

        for muscle_group in workout_split_order[index]:  
            group_order = get_dynamic_workout_order(time, muscle_group)
            daily_workout = generate_workout(group_order, equipment, difficulty, connection, limitations, muscle_group)
            workout_plan.append(daily_workout)

        print({"days": workout_plan})

        return jsonify({"days": workout_plan})

    else:
        # Daily workout generation
        muscle_split = data["muscleSplit"]
        group_order = get_dynamic_workout_order(time, muscle_split)

        # Ensure group_order is not None
        if group_order is None:
            return jsonify({"error": "Invalid muscleSplit provided."}), 400

        workout_plan = generate_workout(group_order, equipment, difficulty, connection, limitations, muscle_split)

        print({"days": [workout_plan]})
        return jsonify({"days": [workout_plan]})

def generate_workout(group_order, equipment, difficulty, connection, limitations, muscle_group):
    """Generate a workout based on provided parameters."""

    workout_plan = []
    selected_exercises = set()
    weight = 4
    count = 0

    for muscle_to_hit in group_order:
        exercise = choose_an_exercise(
            muscle_to_hit[0], muscle_to_hit[1], equipment, difficulty, muscle_to_hit[2],
            connection, selected_exercises, limitations, weight
        )
        if exercise:
            workout_plan.append(exercise)
            selected_exercises.add(exercise["Parent Exercise"])

        count += 1
        if count % 3 == 0:
            weight -= 1

    return {"type": muscle_group, "workout_data": workout_plan}

def choose_an_exercise(muscle_to_hit, muscle_subgroup, equipment_list, workout_experience, is_compound, connection, selected_exercises, limitations, weight):
    """Return one exercise chosen, ensuring no repetitions."""

    workouts_to_pick_from = []

    sql_query = """
    SELECT name, parent_exercise, movement_type FROM exercises
    WHERE muscle_group == ? 
    AND weight >= ? 
    AND (difficulty == ? OR difficulty == 3)
    AND is_compound == ?
    """

    # Add equipment to the query
    if equipment_list:
        equipment_placeholders = ', '.join('?' * len(equipment_list))
        sql_query += f" AND equipment IN ({equipment_placeholders})"

    # Add main_muscle conditionally
    if muscle_subgroup != "all":
        sql_query += " AND main_muscle == ?"

    # Add limitations conditionally
    if limitations:
        limitation_placeholders = ', '.join('?' * len(limitations))
        sql_query += f" AND movement_type NOT IN ({limitation_placeholders})"

    # Add check for repeats
    if selected_exercises:
        placeholders = ', '.join('?' * len(selected_exercises))
        sql_query += f" AND parent_exercise NOT IN ({placeholders})"

    # Construct the query parameters
    query_params = [muscle_to_hit, weight, workout_experience, is_compound] + equipment_list
    if muscle_subgroup != "all":
        query_params.append(muscle_subgroup)
    query_params += limitations + list(selected_exercises)

    # Execute the query
    cur = connection.execute(sql_query, query_params)
    query_result = cur.fetchall()

    if query_result:
        for result in query_result:
            reps = (workout_experience * 30) + 30 if result['movement_type'] == "plank" else "10"
            workouts_to_pick_from.append({
                "Exercise": result['name'],
                "Sets": "3",
                "Reps": reps,
                "Parent Exercise": result['parent_exercise']
            })

    return random.choice(workouts_to_pick_from) if workouts_to_pick_from else None

def save_workout(req):
    """Save the last generated workout to the database."""
    
    # Get the JSON payload from the request
    json_data = req.get_json()
    
    # Check that the workouts data is present in the JSON payload
    if not json_data or "workouts" not in json_data:
        return jsonify({"error": "Invalid request. Missing workouts data"}), 400

    # Retrieve the username from the cookies
    username = req.cookies.get("username")
    if not username:
        return jsonify({"error": "User not authenticated"}), 401

    # Convert the workouts data to a JSON string for storing in the DB
    workout_json = json.dumps(json_data["workouts"])

    connection = get_db()
    connection.execute(
        "INSERT INTO saved_workouts (username, workout_data) VALUES (?, ?)",
        (username, workout_json)
    )
    connection.commit()

    return jsonify({"message": "Workout saved successfully!"}), 201

def get_last_workout(req):
    """Retrieve the last saved workout from the database."""

    connection = get_db()
    username = req.cookies.get("username")
    cur = connection.execute(
        "SELECT workout_data FROM saved_workouts WHERE username = ? ORDER BY id DESC LIMIT 1",
        (username,)
    )
    workout = cur.fetchone()

    if workout:
        return jsonify(json.loads(workout["workout_data"]))
    else:
        return jsonify({"error": "No saved workouts found."}), 404


workout_split_order = [
    ("full", "full"),
    ("full","full","full"),
    ("upper","legs","upper","legs"),
    ("upper","legs","upper","legs","shoulders"),
    ("push","pull","legs","push","pull","legs"),
    ]