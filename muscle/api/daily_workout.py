"""REST API to generate workouts."""
import flask
import muscle
import json
import random


def generate_daily_workout(time, equipment, muscle_group, workout_type, difficulty, connection, limitations):
    """Generate a daily workout for the user."""

    if muscle_group == "full":
        return flask.jsonify(generate_daily_fullbody_workout(time, equipment, workout_type, difficulty, connection, limitations))

    elif muscle_group == "push":
        return flask.jsonify(generate_daily_push_workout(time, equipment, workout_type, difficulty, connection, limitations))

    elif muscle_group == "pull":
        return flask.jsonify(generate_daily_pull_workout(time, equipment, workout_type, difficulty, connection, limitations))

    elif muscle_group == "legs" or muscle_group == "lower":
        return flask.jsonify(generate_daily_lower_workout(time, equipment, workout_type, difficulty, connection, limitations))

    elif muscle_group == "upper":
        return flask.jsonify(generate_daily_upper_workout(time, equipment, workout_type, difficulty, connection, limitations))

    elif muscle_group == "chest":
        return flask.jsonify(generate_daily_chest_workout(time, equipment, workout_type, difficulty, connection, limitations))

    elif muscle_group == "back":
        return flask.jsonify(generate_daily_back_workout(time, equipment, workout_type, difficulty, connection, limitations))

    elif muscle_group == "arms":
        return flask.jsonify(generate_daily_arm_workout(time, equipment, workout_type, difficulty, connection, limitations))

    elif muscle_group == "triceps" or muscle_group == "biceps":
        return flask.jsonify(generate_daily_tri_bi_workout(time, equipment, workout_type, difficulty, connection, limitations, muscle_group))

    elif muscle_group == "abs":
        return flask.jsonify(generate_daily_ab_workout(time, equipment, workout_type, difficulty, connection, limitations))
    
    elif muscle_group == "shoulders":
        return flask.jsonify(generate_daily_shoulder_workout(time, equipment, workout_type, difficulty, connection, limitations))
    
    else:
        return flask.jsonify(generate_other_workout(time, equipment, workout_type, difficulty, connection, limitations))


def generate_daily_fullbody_workout(time, equipment, workout_type, difficulty, connection, limitations):
    """Make a daily fullbody workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout
    legs_muscles_list = ["legs", "glutes", "hamstrings", "quads"]
    chest_muscles_list = ["chest", "upper-chest"]
    back_muscles_list = ["mid-back", "upper-back", "lats"]
    sets = 3
    weight = 3

    if time == "30":
        group_order = [("legs", "legs", 3, 8,  "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("back", random.choice(back_muscles_list), 3, 8, "compound")]

    elif time == "45":
        group_order = [("legs", "legs", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("back", random.choice(back_muscles_list), 3, 8, "compound"),
                       ("triceps", "triceps", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")]

    elif time == "60":
        group_order = [("legs", "legs", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("back", random.choice(back_muscles_list), 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("triceps", "triceps", 3, 12, "isolation"),
                       ("biceps", "biceps", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")]

    elif time == "75":
        group_order = [("legs", "legs", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("back", random.choice(back_muscles_list), 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("triceps", "triceps", 3, 12, "isolation"),
                       ("biceps", "biceps", 3, 12, "isolation"),
                       ("legs", "calves", 3, 16, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")]

    elif time == "90":
        group_order = [("legs", "legs", 3, 8),
                       ("chest", "chest", 3, 8),
                       ("back", random.choice(back_muscles_list), 3, 8),
                       ("legs", random.choice(legs_muscles_list), 3, 8),
                       ("chest", random.choice(chest_muscles_list), 3, 8),
                       ("back", random.choice(back_muscles_list), 3, 8),
                       ("abs", "abs", 3, 12)]
    elif time == "105":
        group_order = [("legs", "legs", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("back", random.choice(back_muscles_list), 3, 8, "compound"),
                       ("legs", random.choice(legs_muscles_list), 3, 8, "compound"),
                       ("chest", random.choice(chest_muscles_list), 3, 8, "compound"),
                       ("back", random.choice(back_muscles_list), 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("abs", "abs", 3, 12, "isolation")]

    elif time == "120":
        group_order = [("legs", "legs", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("back", random.choice(back_muscles_list), 3, 8, "compound"),
                       ("legs", random.choice(legs_muscles_list), 3, 8, "compound"),
                       ("chest", random.choice(chest_muscles_list), 3, 8, "compound"),
                       ("back", random.choice(back_muscles_list), 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("biceps", "biceps", 3, 12, "isolation"),
                       ("triceps", "triceps", 3, 12, "isolation"),
                       ("abs", "abs", 3, 8, "isolation")]

    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations)


def generate_daily_push_workout(time, equipment, workout_type, difficulty, connection, limitations):
    """Make a daily push workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout
    chest_muscles_list = ["chest", "upper-chest"]
    shoulders_muscles_list = ["shoulders", "lateral", "anterior", "rear"]
    sets = 3
    weight = 3

    if time == "30":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("triceps", "triceps", 3, 12, "isolation")]

    elif time == "45":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 12, "isolation")]

    elif time == "60":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("triceps", "triceps", 3, 12, "isolation")]

    elif time == "75":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("shoulders", "lateral", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 12, "isolation")]

    elif time == "90":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("shoulders", "lateral", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 12, "isolation"),
                       ("triceps", "triceps", 3, 12, "isolation")]

    elif time == "105":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("chest", "upper-chest", 3, 8, "isolation"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("shoulders", "lateral", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 12, "isolation"),
                       ("triceps", "triceps", 3, 12, "isolation")]

    elif time == "120":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("chest", "upper-chest", 3, 8, "isolation"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("shoulders", "lateral", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 12, "isolation"),
                       ("triceps", "triceps", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")]

    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations)


def generate_daily_pull_workout(time, equipment, workout_type, difficulty, connection, limitations):
    """Make a daily push workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout
    back_muscles_list = ["mid-back", "upper-back", "lats"]
    weight = 3

    if time == "30":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("biceps", "biceps", 3, 12, "isolation")]

    elif time == "45":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("biceps", "bicpes", 3, 12, "isolation")]

    elif time == "60":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("shoulders", "rear", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 12, "isolation")]

    elif time == "75":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("shoulders", "rear", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")]

    elif time == "90":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "isolation"),
                       ("shoulders", "rear", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 12, "isolation"),
                       ("biceps", "biceps", 3, 12, "isolation")]

    elif time == "105":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", "upper-back", 3, 8, "isolation"),
                       ("shoulders", "rear", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 12, "isolation"),
                       ("biceps", "biceps", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")]

    elif time == "120":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", "upper-back", 3, 8, "isolation"),
                       ("shoulders", "rear", 3, 8, "isolation"),
                       ("shoulders", "rear", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 12, "isolation"),
                       ("biceps", "biceps", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")]

    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations)


def generate_daily_lower_workout(time, equipment, workout_type, difficulty, connection, limitations):
    """Make a daily push workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout
    legs_muscles_list = ["legs", "quads", "glutes", "hamstrings"]
    weight = 3

    if time == "30":
        group_order = [("legs", "legs", 3, 5, "compound"),
                       ("legs", random.choice(legs_muscles_list), 3, 8, "compound"),
                       ("legs", random.choice(legs_muscles_list), 3, 8, "compound")]

    elif time == "45":
        group_order = [("legs", "legs", 3, 5, "compound"),
                       ("legs", "quads", 3, 8, "compound"),
                       ("legs", "hamstrings", 3, 8, "compound"),
                       ("legs", "calves", 3, 12, "isolation")
                       ]

    elif time == "60":
        group_order = [("legs", "legs", 3, 5, "compound"),
                       ("legs", "glutes", 3, 8, "compound"),
                       ("legs", "quads", 3, 8, "compound"),
                       ("legs", "hamstrings", 3, 8, "compound"),
                       ("legs", "calves", 3, 12, "isolation")
                       ]

    elif time == "75":
        group_order = [("legs", "legs", 3, 5, "compound"),
                       ("legs", random.choice(legs_muscles_list), 3, 8, "compound"),
                       ("legs", "glutes", 3, 8, "compound"),
                       ("legs", "quads", 3, 8, "compound"),
                       ("legs", "hamstrings", 3, 8, "isolation"),
                       ("legs", "calves", 3, 12, "isolation")
                       ]

    elif time == "90":
        group_order = [("legs", "legs", 3, 5, "compound"),
                       ("legs", random.choice(legs_muscles_list), 3, 8, "compound"),
                       ("legs", "glutes", 3, 8, "compound"),
                       ("legs", "quads", 3, 8, "isolation"),
                       ("legs", "hamstrings", 3, 8, "isolation"),
                       ("legs", "calves", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")
                       ]

    elif time == "105":
        group_order = [("legs", "legs", 3, 5, "compound"),
                       ("legs", random.choice(legs_muscles_list), 3, 8, "compound"),
                       ("legs", "glutes", 3, 8, "compound"),
                       ("legs", random.choice(legs_muscles_list), 3, 8, "compound"),
                       ("legs", "quads", 3, 8, "isolation"),
                       ("legs", "hamstrings", 3, 8, "isolation"),
                       ("legs", "calves", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")
                       ]

    elif time == "120":
        group_order = [("legs", "legs", 3, 5, "compound"),
                       ("legs", random.choice(legs_muscles_list), 3, 8, "compound"),
                       ("legs", "glutes", 3, 8, "compound"),
                       ("legs", "quads", 3, 8, "compound"),
                       ("legs", "hamstrings", 3, 8, "compound"),
                       ("legs", random.choice(legs_muscles_list), 3, 8, "isolation"),
                       ("legs", random.choice(legs_muscles_list), 3, 8, "isolation"),
                       ("legs", "calves", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")
                       ]

    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations)


def generate_daily_upper_workout(time, equipment, workout_type, difficulty, connection, limitations):
    """Make a daily push workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout
    back_muscles_list = ["upper-back", "mid-back", "lats"]
    shoulders_muscles_list = ["shoulders", "anterior", "rear", "lateral"]
    chest_muscles_list = ["chest", "upper-chest"]

    weight = 3

    if time == "30":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("back", "mid-back", 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound")]

    elif time == "45":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("back", "mid-back", 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("abs", "abs", 3, 12, "isolation")]

    elif time == "60":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("back", "mid-back", 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("abs", "abs", 3, 12, "isolation")]

    elif time == "75":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("back", "mid-back", 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("biceps", "biceps", 3, 8, "compound"),
                       ("abs", "abs", 3, 12, "isolation")]

    elif time == "90":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("back", "mid-back", 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("biceps", "biceps", 3, 12, "isolation"),
                       ("triceps", "triceps", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")]

    elif time == "105":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("back", "mid-back", 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("biceps", "biceps", 3, 12, "isolaton"),
                       ("triceps", "triceps", 3, 12, "isolation"),
                       ("shoulders", "rear", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")]

    elif time == "120":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("back", "mid-back", 3, 8, "compound"),
                       ("shoulders", "shoulders", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("biceps", "biceps", 3, 12, "isolation"),
                       ("triceps", "triceps", 3, 12, "isolation"),
                       ("shoulders", "rear", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation"),
                       ("abs", "abs", 3, 12, "isolation")
                       ]

    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations)


def generate_daily_chest_workout(time, equipment, workout_type, difficulty, connection, limitations):
    """Make a daily push workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout

    chest_muscles_list = ["chest", "upper-chest", "lower-chest"]

    weight = 3

    if time == "30":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", random.choice(chest_muscles_list), 3, 8, "compound")]

    elif time == "45":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", random.choice(chest_muscles_list), 3, 8, "compound"),
                       ("chest", random.choice(chest_muscles_list), 3, 8, "isolation")]

    elif time == "60":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", random.choice(chest_muscles_list), 3, 8, "isolation")]

    elif time == "75":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "lower-chest", 3, 8, "compound"),
                       ("chest", random.choice(chest_muscles_list), 3, 8, "isolation")]

    elif time == "90":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "lower-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "isolation"),
                       ("chest", random.choice(chest_muscles_list), 3, 8, "isolation")]

    elif time == "105":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "lower-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "isolation"),
                       ("chest", "upper-chest", 3, 8, "isolation"),
                       ("chest", random.choice(chest_muscles_list), 3, 8, "isolation")]

    elif time == "120":
        group_order = [("chest", "chest", 3, 5, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "compound"),
                       ("chest", "upper-chest", 3, 8, "compound"),
                       ("chest", "lower-chest", 3, 8, "compound"),
                       ("chest", "chest", 3, 8, "isolation"),
                       ("chest", "upper-chest", 3, 8, "isolation"),
                       ("chest", "upper-chest", 3, 8, "isolation"),
                       ("chest", random.choice(chest_muscles_list), 3, 8, "isolation")]

    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations)


def generate_daily_back_workout(time, equipment, workout_type, difficulty, connection, limitations):
    """Make a daily push workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout

    back_muscles_list = ["back", "upper-back",
                         "mid-back", "lower-back", "lats"]

    weight = 3

    if time == "30":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound")]

    elif time == "45":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", random.choice(back_muscles_list), 3, 8, "isolation")]

    elif time == "60":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", random.choice(back_muscles_list), 3, 8, "isolation")]

    elif time == "75":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lower-back", 3, 8, "isolation"),
                       ("back", random.choice(back_muscles_list), 3, 8, "isolation")]

    elif time == "90":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", "mid-back", 3, 8, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", "lower-back", 3, 8, "isolation")]

    elif time == "105":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", "mid-back", 3, 8, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", random.choice(back_muscles_list), 3, 8, "isolation"),
                       ("back", random.choice(back_muscles_list), 3, 8, "isolation")]

    elif time == "120":
        group_order = [("back", "mid-back", 3, 5, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", "mid-back", 3, 8, "compound"),
                       ("back", "upper-back", 3, 8, "compound"),
                       ("back", "lats", 3, 8, "compound"),
                       ("back", "mid-back", 3, 8, "isolation"),
                       ("back", "upper-back", 3, 8, "isolation"),
                       ("back", "lats", 3, 8, "isolation")]

    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations)

def generate_daily_arm_workout(time, equipment, workout_type, difficulty, connection, limitations):
    """Make a daily push workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout

    weight = 3

    if time == "30":
        group_order = [("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation")
                       ]

    elif time == "45":
        group_order = [("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation")
                       ]

    elif time == "60":
        group_order = [("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation")
                       ]

    elif time == "75":
        group_order = [("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation")
                       ]

    elif time == "90":
        group_order = [("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation")
                       ]

    elif time == "105":
         group_order = [("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation")
                       ]

    elif time == "120":
        group_order = [("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation"),
                       ("triceps", "triceps", 3, 8, "isolation"),
                       ("biceps", "biceps", 3, 8, "isolation")
                       ]

    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations)

def generate_daily_tri_bi_workout(time, equipment, workout_type, difficulty, connection, limitations, muscle_group):
    """Make a daily push workout."""

    # different areas of body parts that can be hit
    # group order is the order of muscle groups in a workout

    weight = 3

    if time == "30":
        group_order = [(muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation")
                       ]

    elif time == "45":
        group_order = [(muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation")
                       ]

    elif time == "60":
        group_order = [(muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation")
                       ]

    elif time == "75":
        group_order = [(muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation")
                       ]

    elif time == "90":
        group_order = [(muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation")
                       ]

    elif time == "105":
         group_order = [(muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation")
                       ]

    elif time == "120":
        group_order = [(muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation"),
                       (muscle_group, muscle_group, 3, 8, "isolation")
                       ]

    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations)

def generate_daily_ab_workout(time, equipment, workout_type, difficulty, connection, limitations):
    """Make a daily push workout."""

    weight = 3

    if time == "30":
        group_order = [("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation")
                       ]

    elif time == "45":
        group_order = [("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation")
                       ]

    elif time == "60":
        group_order = [("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation")
                       ]

    elif time == "75":
        group_order = [("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation")
                       ]

    elif time == "90":
        group_order = [("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation")
                       ]

    elif time == "105":
         group_order = [("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation")
                       ]

    elif time == "120":
        group_order = [("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation"),
                       ("abs", "abs", 3, 8, "isolation")
                       ]

    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations)

def generate_daily_shoulder_workout(time, equipment, workout_type, difficulty, connection, limitations):
    """Make a daily push workout."""
    

    shoulder_muscle_list = ["shoulder", "rear", "anterior", "lateral"]
    weight = 3

    if time == "30":
        group_order = [("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "isolation")
                       ]

    elif time == "45":
        group_order = [("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "isolation"),
                       ("shoulder", "rear", 3, 8, "isolation")
                       ]

    elif time == "60":
        group_order = [("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "isolation"),
                       ("shoulder", "rear", 3, 8, "isolation")
                       ]

    elif time == "75":
        group_order = [("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "isolation"),
                       ("shoulder", "rear", 3, 8, "isolation"),
                       ("shoulder", "lateral", 3, 8, "isolation")
                       ]

    elif time == "90":
        group_order = [("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "compound"),
                       ("shoulder", "rear", 3, 8, "isolation"),
                       ("shoulder", "lateral", 3, 8, "isolation"),
                       ("shoulder", "rear", 3, 8, "isolation")
                       ]

    elif time == "105":
        group_order = [("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "compound"),
                       ("shoulder", "rear", 3, 8, "isolation"),
                       ("shoulder", "lateral", 3, 8, "isolation"),
                       ("shoulder", "anterior", 3, 8, "isolation"),
                       ("shoulder", "rear", 3, 8, "isolation")
                       ]

    elif time == "120":
        group_order = [("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", "shoulder", 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "compound"),
                       ("shoulder", random.choice(shoulder_muscle_list), 3, 8, "compound"),
                       ("shoulder", "rear", 3, 8, "isolation"),
                       ("shoulder", "lateral", 3, 8, "isolation"),
                       ("shoulder", "anterior", 3, 8, "isolation"),
                       ("shoulder", "rear", 3, 8, "isolation")
                       ]
    return generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations)

def generate_workout(group_order, equipment, workout_type, difficulty, weight, connection, limitations):
    """Generate workout based on time and group order."""

    workout_plan = []
    selected_exercises = set()  # Set to keep track of selected exercises

    for muscle_to_hit in group_order:
        exercise = choose_an_exercise(
            muscle_to_hit[0], muscle_to_hit[1], equipment, workout_type, difficulty, muscle_to_hit[4], weight, connection, selected_exercises, muscle_to_hit[2], muscle_to_hit[3], limitations)
        if exercise:  # Only add if an exercise was found and not already selected
            workout_plan.append(exercise)
            # Add the selected exercise to the set
            selected_exercises.add(exercise["Exercise"])

    workout = {"workout": workout_plan}
    return workout


def choose_an_exercise(muscle_to_hit, muscle_subgroup, equipment_list, workout_type, workout_experience, is_compound, weight, connection, selected_exercises, sets, reps, limitations):
    """Return one exercise chosen, ensuring no repetitions."""

    workouts_to_pick_from = []

    # here I am breaking the set into a comma-separated string to parse through in sql query
    # and generating the correct amount of ?'s to prevent SQL injections
    placeholders = ', '.join('?' * len(selected_exercises))
    limitation_placeholders = ', '.join('?' * len(limitations))

    for equipment in equipment_list:
        sql_query = """
            SELECT name FROM exercises
            WHERE muscle_group == ? 
            AND main_muscle == ? 
            AND type == ? 
            AND weight >= ? 
            AND equipment == ? 
            AND difficulty <= ? 
            AND is_compound == ?
            """
        if limitations:
            sql_query += f"AND movement_type NOT IN ({limitation_placeholders})"
        if selected_exercises:
            # This is added to the query only to check for repeats
            sql_query += f"AND name NOT IN ({placeholders})"

        query_params = [muscle_to_hit, muscle_subgroup, workout_type, weight, equipment,
                        workout_experience, is_compound] + limitations + list(selected_exercises)
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
