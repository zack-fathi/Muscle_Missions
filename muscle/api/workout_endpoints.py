"""REST API to generate workouts."""
import flask
import muscle
import json
import random


def generate_daily_workout(time, equipment, muscle_group, workout_type, difficulty, connection):
    """Generate a daily workout for the user."""

    if muscle_group == "full":
        return generate_daily_fullbody_workout(time, equipment, workout_type, difficulty, connection)

    elif muscle_group == "push":
        return generate_daily_push_workout(time, equipment, workout_type, difficulty, connection)

    elif muscle_group == "pull":
        return generate_daily_pull_workout(time, equipment, workout_type, difficulty, connection)

    elif muscle_group == "legs" or muscle_group == "lower":
        return generate_daily_lower_workout(time, equipment, workout_type, difficulty, connection)

    elif muscle_group == "upper":
        return generate_daily_upper_workout(time, equipment, workout_type, difficulty, connection)

    else:
        return generate_other_workout(time, equipment, workout_type, difficulty, connection)


def generate_daily_fullbody_workout(time, equipment, workout_type, difficulty, connection):
    """Make a daily fullbody workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout
    legs_muscles_list = ["legs", "glutes", "hamstrings", "quads"]
    chest_muscles_list = ["chest", "upper-chest"]
    back_muscles_list = ["mid-back", "upper-back", "lats"]
    sets = 3
    weight = 3

    if time == "30":
        group_order = [("legs", "legs", 3, 8),
                       ("chest", "chest", 3, 8),
                       ("back", random.choice(back_muscles_list), 3, 8)]

    elif time == "45":
        group_order = [("legs", "legs",3 , 8),
                       ("chest", "chest",3, 8),
                       ("back", random.choice(back_muscles_list),3, 8),
                       ("triceps", "triceps",3, 12),
                       ("abs", "abs", 3, 12)]

    elif time == "60":
        group_order = [("legs", "legs",3, 8),
                       ("chest", "chest",3, 8),
                       ("back", random.choice(back_muscles_list),3, 8),
                       ("shoulders", "shoulders",3, 8),
                       ("triceps", "triceps",3, 12),
                       ("biceps", "biceps",3, 12),
                       ("abs", "abs",3, 12)]

    elif time == "75":
        group_order = [("legs", "legs",3, 8),
                       ("chest", "chest",3, 8),
                       ("back", random.choice(back_muscles_list),3, 8),
                       ("shoulders", "shoulders",3, 8),
                       ("triceps", "triceps",3, 12),
                       ("biceps", "biceps",3, 12),
                       ("legs", "calves",3, 16),
                       ("abs", "abs",3, 12)]

    elif time == "90":
        group_order = [("legs", "legs",3, 8),
                       ("chest","chest",3, 8),
                       ("back", random.choice(back_muscles_list),3, 8),
                       ("legs", random.choice(legs_muscles_list),3, 8),
                       ("chest", random.choice(chest_muscles_list),3, 8),
                       ("back", random.choice(back_muscles_list),3, 8),
                       ("abs", "abs",3, 12)]
    elif time == "105":
        group_order = [("legs", "legs",3, 8),
                       ("chest", "chest",3, 8),
                       ("back", random.choice(back_muscles_list),3, 8),
                       ("legs", random.choice(legs_muscles_list),3, 8),
                       ("chest", random.choice(chest_muscles_list),3, 8),
                       ("back", random.choice(back_muscles_list),3, 8),
                       ("shoulders", "shoulders",3, 8),
                       ("abs", "abs",3, 12)]

    elif time == "120":
        group_order = [("legs", "legs",3, 8),
                       ("chest", "chest",3, 8),
                       ("back", random.choice(back_muscles_list),3, 8),
                       ("legs", random.choice(legs_muscles_list),3, 8),
                       ("chest", random.choice(chest_muscles_list),3, 8),
                       ("back", random.choice(back_muscles_list),3, 8),
                       ("shoulders", "shoulders",3, 8),
                       ("biceps", "biceps",3, 12),
                       ("triceps", "triceps",3, 12),
                       ("abs", "abs",3, 8)]

    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection)

def generate_daily_push_workout(time, equipment, workout_type, difficulty, connection):
    """Make a daily push workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout
    chest_muscles_list = ["chest", "upper-chest"]
    shoulders_muscles_list = ["shoulders", "lateral", "anterior", "rear"]
    sets = 3
    weight = 3

    if time == "30":
        group_order = [("chest", "chest",3, 5),
                       ("chest", "upper-chest",3, 8),
                       ("triceps","triceps", 3, 12 )]

    elif time == "45":
        group_order = [("chest", "chest",3, 5),
                       ("chest", "upper-chest",3, 8),
                       ("chest", "chest",3, 8),
                       ("triceps","triceps",3, 12)]

    elif time == "60":
        group_order = [("chest", "chest",3, 5),
                       ("chest", "upper-chest",3, 8),
                       ("chest", "chest",3, 8),
                       ("shoulders","shoulders",3, 8),
                       ("triceps","triceps",3, 12)]
        
    elif time == "75":
        group_order = [("chest", "chest",3, 5),
                       ("chest", "upper-chest",3, 8),
                       ("chest", "chest",3, 8),
                       ("shoulders","shoulders",3, 8),
                       ("shoulders","lateral", 3, 8),
                       ("triceps","triceps", 3, 12)]

    elif time == "90":
        group_order = [("chest", "chest",3, 5),
                       ("chest", "upper-chest",3, 8),
                       ("chest", "chest",3, 8),
                       ("shoulders","shoulders",3, 8),
                       ("shoulders","lateral", 3, 8),
                       ("triceps","triceps",3, 12),
                       ("triceps","triceps",3, 12)]
        
    elif time == "105":
        group_order = [("chest", "chest",3, 5),
                       ("chest", "upper-chest",3, 8),
                       ("chest", "chest",3, 8),
                       ("chest", "upper-chest",3, 8),
                       ("shoulders","shoulders",3, 8),
                       ("shoulders","lateral", 3, 8),
                       ("triceps","triceps",3, 12),
                       ("triceps","triceps",3, 12)]

    elif time == "120":
        group_order = [("chest", "chest",3, 5),
                       ("chest", "upper-chest",3, 8),
                       ("chest", "chest",3, 8),
                       ("chest", "upper-chest",3, 8),
                       ("shoulders","shoulders",3, 8),
                       ("shoulders","lateral", 3, 8),
                       ("triceps","triceps",3, 12),
                       ("triceps","triceps",3, 12),
                       ("abs", "abs", 3, 12)]


    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection)

def generate_daily_pull_workout(time, equipment, workout_type, difficulty, connection):
    """Make a daily push workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout
    back_muscles_list = ["mid-back", "upper-back", "lats"]
    weight = 3

    if time == "30":
        group_order = [("back", "mid-back",3, 5),
                       ("back", "lats",3, 8),
                       ("biceps","biceps", 3, 12 )]

    elif time == "45":
        group_order = [("back", "mid-back",3, 5),
                       ("back", "upper-back",3, 8),
                       ("back", "lats",3, 8),
                       ("bicpes","bicpes",3, 12)]

    elif time == "60":
        group_order = [("back", "mid-back",3, 5),
                       ("back", "upper-back",3, 8),
                       ("back", "lats",3, 8),
                       ("shoulders","rear",3, 8),
                       ("biceps","biceps",3, 12)]
        
    elif time == "75":
        group_order = [("back", "mid-back",3, 5),
                       ("back", "upper-back",3, 8),
                       ("back", "lats",3, 8),
                       ("shoulders","rear",3, 8),
                       ("biceps","biceps", 3, 8),
                       ("abs","abs", 3, 12)]

    elif time == "90":
        group_order = [("back", "mid-back",3, 5),
                       ("back", "upper-back",3, 8),
                       ("back", "lats",3, 8),
                       ("back","lats",3, 8),
                       ("shoulders","rear", 3, 8),
                       ("biceps","biceps",3, 12),
                       ("biceps","biceps",3, 12)]
        
    elif time == "105":
        group_order = [("back", "mid-back",3, 5),
                       ("back", "upper-back",3, 8),
                       ("back", "lats",3, 8),
                       ("back", "upper-back",3, 8),
                       ("shoulders","rear",3, 8),
                       ("biceps","biceps",3, 12),
                       ("biceps","biceps",3, 12),
                       ("abs","abs", 3, 12)]

    elif time == "120":
        group_order = [("back", "mid-back",3, 5),
                       ("back", "upper-back",3, 8),
                       ("back", "lats",3, 8),
                       ("back", "upper-back",3, 8),
                       ("shoulders","rear",3, 8),
                       ("shoulders","rear", 3, 8),
                       ("biceps","biceps",3, 12),
                       ("biceps","biceps",3, 12),
                       ("abs", "abs", 3, 12)]


    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection)


def generate_workout(group_order, equipment, workout_type, difficulty, weight, connection):
    """Generate workout based on time and group order."""

    workout_plan = []
    selected_exercises = set()  # Set to keep track of selected exercises

    for muscle_to_hit in group_order:
        exercise = choose_an_exercise(
            muscle_to_hit[0], muscle_to_hit[1], equipment, workout_type, difficulty, weight, connection, selected_exercises, muscle_to_hit[2], muscle_to_hit[3])
        if exercise:  # Only add if an exercise was found and not already selected
            workout_plan.append(exercise)
            # Add the selected exercise to the set
            selected_exercises.add(exercise["Exercise"])

    workout = {"workout": workout_plan}
    return flask.jsonify(workout)


def generate_45_minute_workou(time, equipment, workout_type, difficulty, connection):
    """Make a daily lower workout."""


def generate_60_minute_workou(time, equipment, workout_type, difficulty, connection):
    """Make a daily push workout."""


def generate_75_minute_workou(time, equipment, workout_type, difficulty, connection):
    """Make a daily pull workout."""


def generate_90_minute_workou(time, equipment, workout_type, difficulty, connection):
    """Make a daily workout."""


def generate_105_minute_workou(time, equipment, workout_type, difficulty, connection):
    """Make a daily workout."""


def generate_120_minute_workou(time, equipment, workout_type, difficulty, connection):
    """Make a daily workout."""


def choose_an_exercise(muscle_to_hit, muscle_subgroup, equipment_list, workout_type, workout_experience, weight, connection, selected_exercises,sets, reps):
    """Return one exercise chosen, ensuring no repetitions."""

    workouts_to_pick_from = []

    # here I am breaking the set into a comma-separated string to parse through in sql query
    # and generating the correct amount of ?'s to prevent SQL injections
    placeholders = ', '.join('?' * len(selected_exercises))

    for equipment in equipment_list:
        sql_query = """
            SELECT name FROM exercises
            WHERE muscle_group == ? AND main_muscle == ? AND type == ? AND weight >= ? AND equipment == ? AND difficulty <= ?
            """
        if selected_exercises:
            # This is added to the query only to check for repeats
            sql_query += f"AND name NOT IN ({placeholders})"
        
        query_params = [muscle_to_hit, muscle_subgroup, workout_type, weight, equipment, workout_experience] + list(selected_exercises)
        cur = connection.execute(sql_query, query_params)
        query_result = cur.fetchall()

        if query_result:
            for result in query_result:
                workouts_to_pick_from.append({"Exercise": result['name'],
                                              "Sets": sets,
                                              "Reps": reps})

    if workouts_to_pick_from:
        return random.choice(workouts_to_pick_from)
    else:
        return None