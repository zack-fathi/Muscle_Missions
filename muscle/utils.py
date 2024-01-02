"""Useful functions across all files."""

import flask
import random
import muscle
from enum import Enum


legs_muscles_list = ["legs", "glutes", "hamstrings", "quads"]
chest_muscles_list = ["chest", "upper-chest"]
back_muscles_list = ["mid-back", "upper-back", "lats"]
shoulder_muscle_list = ["shoulders", "lateral", "anterior", "rear"]


def clear_cookie():
    """Clear a cookie if removed from database."""
    response = flask.make_response(flask.redirect(
        '/accounts/login/'))  # Redirect or return a response
    response.set_cookie('username', '', expires=0)  # Clear the cookie
    return response


def check_logname_exists():
    """Check if logname exists."""

    connection = muscle.model.get_db()
    logname = flask.request.cookies.get('username', None)

    if not logname:
        return False

    cur = connection.execute(
        "SELECT username from users "
        "WHERE username == ? ",
        (logname,)
    )

    if not cur.fetchone:
        return False

    return True

def get_exercise_id_by_name(exercise_name):
    """Get exercise ID."""
    connection = muscle.model.get_db()
    cur = connection.execute(
        "SELECT exerciseID FROM exercises WHERE name = ?",
        (exercise_name,)
    )
    result = cur.fetchone()
    if result:
        return result['exerciseID']
    else:
        return None


def get_user_id(connection):
    """Get a user ID."""
    logname = flask.request.cookies.get('username')
    cur = connection.execute(
        "SELECT userID FROM users WHERE username = ?",
        (logname,)
    )
    result = cur.fetchone()
    if result:
        return result['userID']
    else:
        return None


def get_difficulty(connection):
    """Get a user's difficulty."""

    logname = flask.request.cookies.get('username')

    cur = connection.execute(
        "SELECT workout_experience "
        "FROM users "
        "WHERE username == ?",
        (logname,)
    )

    return cur.fetchone()['workout_experience']


workout_split_shortcuts = {

    "full": "Full Body",
    "upper": "Upper Body", 
    "lower": "Lower Body",
    "legs": "Legs",
    "push": "Push",
    "pull": "Pull",
    "shoulders": "Shoulders",
    "arms": "Arms"
}


workout_split_order = [
    ("full", "full"),
    ("full","full","full"),
    ("upper","legs","upper","legs"),
    ("upper","legs","upper","legs","shoulders"),
    ("push","pull","legs","push","pull","legs"),
    ]

def get_dynamic_workout_order(time, workout_type):
    """Get a random workout order."""

    if workout_type == "full":
        if time == "30":
            return [("legs", "all", "compound"), ("chest", "chest", "compound"),
               ("back", "all", "compound")]
        
        elif time == "45":
            return [("legs", "all", "compound"),
               ("chest", "chest", "compound"),
               ("back", random.choice(back_muscles_list), "compound"),
               ("arms", "triceps", "isolation"),
               ("abs", "abs", "isolation")]
        
        elif time == "60":
            return [("legs", "all", "compound"),
               ("chest", "chest", "compound"),
               ("back", random.choice(back_muscles_list), "compound"),
               ("shoulders", "shoulders", "compound"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("abs", "abs", "isolation")]

        elif time == "75":
            return [("legs", "all", "compound"),
               ("chest", "chest", "compound"),
               ("back", random.choice(back_muscles_list), "compound"),
               ("shoulders", "shoulders", "compound"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("legs", "calves", "isolation"),
               ("abs", "abs", "isolation")]

        elif time == "90": 
            return [("legs", "all", "compound"),
               ("chest", "chest", "compound"),
               ("back", random.choice(back_muscles_list), "compound"),
               ("legs", "all", "compound"),
               ("chest", random.choice(chest_muscles_list), "compound"),
               ("back", random.choice(back_muscles_list), "compound"),
               ("abs", "abs", "isolation")]

        elif time == "105": 
            return [("legs", "all", "compound"),
                ("chest", "chest", "compound"),
                ("back", random.choice(back_muscles_list), "compound"),
                ("legs", "all", "compound"),
                ("chest", random.choice(chest_muscles_list), "compound"),
                ("back", random.choice(back_muscles_list), "compound"),
                ("shoulders", "shoulders", "compound"),
                ("abs", "abs", "isolation")]

        elif time == "120": 
            return [("legs", "all", "compound"),
                ("chest", "chest", "compound"),
                ("back", random.choice(back_muscles_list), "compound"),
                ("legs", "all", "compound"),
                ("chest", random.choice(chest_muscles_list), "compound"),
                ("back", random.choice(back_muscles_list), "compound"),
                ("shoulders", "shoulders", "compound"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("abs", "abs", "isolation")]
    

    if workout_type == "push": 
        if time == "30": 
            return [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("arms", "triceps", "isolation")]

        elif time == "45": 
            return [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "isolation"),
               ("arms", "triceps", "isolation")]

        elif time == "60": 
            return [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("arms", "triceps", "isolation")]

        elif time == "75": 
            return [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("shoulders", "lateral", "isolation"),
               ("arms", "triceps", "isolation")]

        elif time =="90": 
            return [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("shoulders", "lateral", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "triceps", "isolation")]

        elif time == "105": 
            return [("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "chest", "compound"),
                ("chest", "upper-chest", "isolation"),
                ("shoulders", "shoulders", "compound"),
                ("shoulders", "lateral", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "triceps", "isolation")]

        elif time == "120": 
            return [("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "chest", "compound"),
                ("chest", "upper-chest", "isolation"),
                ("shoulders", "shoulders", "compound"),
                ("shoulders", "lateral", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("abs", "abs", "isolation")]

    if workout_type == "pull": 
        if time == "30": 
            return [("back", "mid-back", "compound"),
               ("back", "lats", "compound"),
               ("arms", "biceps", "isolation")]

        elif time == "45": 
            return [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("arms", "biceps", "isolation")]

        elif time == "60": 
            return [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("shoulders", "rear", "isolation"),
               ("arms", "biceps", "isolation")]

        elif time == "75": 
            return [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("shoulders", "rear", "isolation"),
               ("arms", "biceps", "isolation"),
               ("abs", "abs", "isolation")]

        elif time == "90": 
            return [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", "lats", "isolation"),
               ("shoulders", "rear", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "biceps", "isolation")]

        elif time == "105": 
            return [("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", "upper-back", "isolation"),
                ("shoulders", "rear", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("abs", "abs", "isolation")]

        elif time == "120": 
            return [("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", "upper-back", "isolation"),
                ("shoulders", "rear", "isolation"),
                ("shoulders", "rear", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("abs", "abs", "isolation")]

    if workout_type == "legs": 
        if time == "30": 
            return [("legs", "legs", "compound"),
               ("legs", random.choice(legs_muscles_list), "compound"),
               ("legs", random.choice(legs_muscles_list), "compound")]

        elif time == "45": 
            return [("legs", "legs", "compound"),
               ("legs", "quads", "compound"),
               ("legs", "hamstrings", "compound"),
               ("legs", "calves", "isolation")
               ]

        elif time == "60":  
            return [("legs", "legs", "compound"),
                ("legs", "glutes", "compound"),
                ("legs", "quads", "compound"),
                ("legs", "hamstrings", "compound"),
                ("legs", "calves", "isolation")
                ]

        elif time == "75": 
            return [("legs", "legs", "compound"),
               ("legs", random.choice(legs_muscles_list), "compound"),
               ("legs", "glutes", "compound"),
               ("legs", "quads", "compound"),
               ("legs", "hamstrings", "isolation"),
               ("legs", "calves", "isolation")
               ]

        elif time == "90": 
            return [("legs", "legs", "compound"),
               ("legs", random.choice(legs_muscles_list), "compound"),
               ("legs", "glutes", "compound"),
               ("legs", "quads", "isolation"),
               ("legs", "hamstrings", "isolation"),
               ("legs", "calves", "isolation"),
               ("abs", "abs", "isolation")
               ]

        elif time == "105": 
            return [("legs", "legs", "compound"),
                ("legs", random.choice(legs_muscles_list), "compound"),
                ("legs", "glutes", "compound"),
                ("legs", random.choice(legs_muscles_list), "compound"),
                ("legs", "quads", "isolation"),
                ("legs", "hamstrings", "isolation"),
                ("legs", "calves", "isolation"),
                ("abs", "abs", "isolation")
                ]

        elif time == "120": 
            return [("legs", "legs", "compound"),
                ("legs", random.choice(legs_muscles_list), "compound"),
                ("legs", "glutes", "compound"),
                ("legs", "quads", "compound"),
                ("legs", "hamstrings", "compound"),
                ("legs", random.choice(legs_muscles_list), "isolation"),
                ("legs", random.choice(legs_muscles_list), "isolation"),
                ("legs", "calves", "isolation"),
                ("abs", "abs", "isolation")
                ]

    if workout_type == "upper": 
        if time == "30": 
            return [("chest", "chest", "compound"),
               ("back", "mid-back", "compound"),
               ("shoulders", "shoulders", "compound")]


        elif time == "45": 
            return [("chest", "chest", "compound"),
               ("back", "mid-back", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("abs", "abs", "isolation")]

        elif time == "60": 
            return [("chest", "chest", "compound"),
               ("back", "mid-back", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("chest", "chest", "compound"),
               ("back", "lats", "compound"),
               ("abs", "abs", "isolation")]

        elif time == "75": 
            return [("chest", "chest", "compound"),
               ("back", "mid-back", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("chest", "chest", "compound"),
               ("back", "lats", "compound"),
               ("arms", "biceps", "compound"),
               ("abs", "abs", "isolation")]

        elif time =="90": 
            return [("chest", "chest", "compound"),
               ("back", "mid-back", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("chest", "chest", "compound"),
               ("back", "lats", "compound"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("abs", "abs", "isolation")]

        elif time == "105": 
            return [("chest", "chest", "compound"),
                ("back", "mid-back", "compound"),
                ("shoulders", "shoulders", "compound"),
                ("chest", "chest", "compound"),
                ("back", "lats", "compound"),
                ("arms", "biceps", "isolaton"),
                ("arms", "triceps", "isolation"),
                ("shoulders", "rear", "isolation"),
                ("abs", "abs", "isolation")]

        elif time == "120": 
            return [("chest", "chest", "compound"),
                ("back", "mid-back", "compound"),
                ("shoulders", "shoulders", "compound"),
                ("chest", "chest", "compound"),
                ("back", "lats", "compound"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("shoulders", "rear", "isolation"),
                ("abs", "abs", "isolation"),
                ("abs", "abs", "isolation")
                ]

    if workout_type == "chest":
        if time == "30": 
            return [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", random.choice(chest_muscles_list), "compound")]

        elif time == "45": 
            return [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", random.choice(chest_muscles_list), "compound"),
               ("chest", random.choice(chest_muscles_list), "isolation")]

        elif time == "60": 
            return [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", random.choice(chest_muscles_list), "isolation")]

        elif time == "75": 
            return [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "lower-chest", "compound"),
               ("chest", random.choice(chest_muscles_list), "isolation")]

        elif time == "90": 
            return [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "lower-chest", "compound"),
               ("chest", "chest", "isolation"),
               ("chest", random.choice(chest_muscles_list), "isolation")]

        elif time == "105": 
            return [("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "lower-chest", "compound"),
                ("chest", "chest", "isolation"),
                ("chest", "upper-chest", "isolation"),
                ("chest", random.choice(chest_muscles_list), "isolation")]

        elif time == "120": 
            return [("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "lower-chest", "compound"),
                ("chest", "chest", "isolation"),
                ("chest", "upper-chest", "isolation"),
                ("chest", "upper-chest", "isolation"),
                ("chest", random.choice(chest_muscles_list), "isolation")]
        
    if workout_type == "back":
        if time == "30": 
            return [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound")]

        elif time == "45": 
            return [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", random.choice(back_muscles_list), "isolation")]


        elif time == "60": 
            return [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", "upper-back", "compound"),
               ("back", random.choice(back_muscles_list), "isolation")]

        elif time == "75": 
            return [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lower-back", "isolation"),
               ("back", random.choice(back_muscles_list), "isolation")]

        elif time == "90": 
            return [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", "lower-back", "isolation")]

        elif time == "105": 
            return [("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", random.choice(back_muscles_list), "isolation"),
                ("back", random.choice(back_muscles_list), "isolation")]

        elif time == "120": 
            return [("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", "mid-back", "isolation"),
                ("back", "upper-back", "isolation"),
                ("back", "lats", "isolation")]

    if workout_type == "arms":
        if time == "30": 
            return [("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation")
               ]

        elif time == "45": 
            return [("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation")
               ]

        elif time == "60": 
            return [("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation")
               ]

        elif time == "75": 
            return [("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation")
               ]

        elif time == "90": 
            return [("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation")
               ]

        elif time == "105": 
            return [("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation")
                ]

        elif time == "120": 
            return [("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation")
                ]

    if workout_type == "shoulders": 
        if time == "30": 
            return [("shoulder", "shoulder", "compound"),
               ("shoulder", "shoulder", "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "isolation")
               ]

        elif time == "45": 
            return [("shoulder", "shoulder", "compound"),
               ("shoulder", "shoulder", "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "isolation"),
               ("shoulder", "rear", "isolation")
               ]


        elif time == "60": 
            return [("shoulder", "shoulder", "compound"),
               ("shoulder", "shoulder", "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "isolation"),
               ("shoulder", "rear", "isolation")
               ]

        elif time == "75": 
            return [("shoulder", "shoulder", "compound"),
               ("shoulder", "shoulder", "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "isolation"),
               ("shoulder", "rear", "isolation"),
               ("shoulder", "lateral", "isolation")
               ]

        elif time == "90": 
            return [("shoulder", "shoulder", "compound"),
               ("shoulder", "shoulder", "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "compound"),
               ("shoulder", "rear", "isolation"),
               ("shoulder", "lateral", "isolation"),
               ("shoulder", "rear", "isolation")
               ]

        elif time == "105": 
            return [("shoulder", "shoulder", "compound"),
                ("shoulder", "shoulder", "compound"),
                ("shoulder", random.choice(
                    shoulder_muscle_list), "compound"),
                ("shoulder", random.choice(
                    shoulder_muscle_list), "compound"),
                ("shoulder", "rear", "isolation"),
                ("shoulder", "lateral", "isolation"),
                ("shoulder", "anterior", "isolation"),
                ("shoulder", "rear", "isolation")
                ]

        elif time == "120": 
            return [("shoulder", "shoulder", "compound"),
                ("shoulder", "shoulder", "compound"),
                ("shoulder", random.choice(
                    shoulder_muscle_list), "compound"),
                ("shoulder", random.choice(
                    shoulder_muscle_list), "compound"),
                ("shoulder", random.choice(
                    shoulder_muscle_list), "compound"),
                ("shoulder", "rear", "isolation"),
                ("shoulder", "lateral", "isolation"),
                ("shoulder", "anterior", "isolation"),
                ("shoulder", "rear", "isolation")
                ]



# this map is the layout of all the workout routines
workout_structures = {
    "full": {
        "30": [("legs", random.choice(legs_muscles_list), "compound"), ("chest", "chest", "compound"),
               ("back", random.choice(back_muscles_list), "compound")],

        "45": [("legs", random.choice(legs_muscles_list), "compound"),
               ("chest", "chest", "compound"),
               ("back", random.choice(back_muscles_list), "compound"),
               ("arms", "triceps", "isolation"),
               ("abs", "abs", "isolation")],
        "60": [("legs", random.choice(legs_muscles_list), "compound"),
               ("chest", "chest", "compound"),
               ("back", random.choice(back_muscles_list), "compound"),
               ("shoulders", "shoulders", "compound"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("abs", "abs", "isolation")],

        "75": [("legs", random.choice(legs_muscles_list), "compound"),
               ("chest", "chest", "compound"),
               ("back", random.choice(back_muscles_list), "compound"),
               ("shoulders", "shoulders", "compound"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("legs", "calves", "isolation"),
               ("abs", "abs", "isolation")],

        "90": [("legs", random.choice(legs_muscles_list), "compound"),
               ("chest", "chest", "compound"),
               ("back", random.choice(back_muscles_list), "compound"),
               ("legs", random.choice(legs_muscles_list), "compound"),
               ("chest", random.choice(chest_muscles_list), "compound"),
               ("back", random.choice(back_muscles_list), "compound"),
               ("abs", "abs", "isolation")],

        "105": [("legs", random.choice(legs_muscles_list), "compound"),
                ("chest", "chest", "compound"),
                ("back", random.choice(back_muscles_list), "compound"),
                ("legs", random.choice(legs_muscles_list), "compound"),
                ("chest", random.choice(chest_muscles_list), "compound"),
                ("back", random.choice(back_muscles_list), "compound"),
                ("shoulders", "shoulders", "compound"),
                ("abs", "abs", "isolation")],

        "120": [("legs", random.choice(legs_muscles_list), "compound"),
                ("chest", "chest", "compound"),
                ("back", random.choice(back_muscles_list), "compound"),
                ("legs", random.choice(legs_muscles_list), "compound"),
                ("chest", random.choice(chest_muscles_list), "compound"),
                ("back", random.choice(back_muscles_list), "compound"),
                ("shoulders", "shoulders", "compound"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("abs", "abs", "isolation")]
    },

    "push": {

        "30": [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("arms", "triceps", "isolation")],

        "45": [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "isolation"),
               ("arms", "triceps", "isolation")],

        "60": [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("arms", "triceps", "isolation")],

        "75": [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("shoulders", "lateral", "isolation"),
               ("arms", "triceps", "isolation")],

        "90": [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("shoulders", "lateral", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "triceps", "isolation")],

        "105": [("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "chest", "compound"),
                ("chest", "upper-chest", "isolation"),
                ("shoulders", "shoulders", "compound"),
                ("shoulders", "lateral", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "triceps", "isolation")],

        "120": [("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "chest", "compound"),
                ("chest", "upper-chest", "isolation"),
                ("shoulders", "shoulders", "compound"),
                ("shoulders", "lateral", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("abs", "abs", "isolation")]
    },

    "pull": {

        "30": [("back", "mid-back", "compound"),
               ("back", "lats", "compound"),
               ("arms", "biceps", "isolation")],

        "45": [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("arms", "biceps", "isolation")],

        "60": [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("shoulders", "rear", "isolation"),
               ("arms", "biceps", "isolation")],

        "75": [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("shoulders", "rear", "isolation"),
               ("arms", "biceps", "isolation"),
               ("abs", "abs", "isolation")],

        "90": [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", "lats", "isolation"),
               ("shoulders", "rear", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "biceps", "isolation")],

        "105": [("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", "upper-back", "isolation"),
                ("shoulders", "rear", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("abs", "abs", "isolation")],

        "120": [("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", "upper-back", "isolation"),
                ("shoulders", "rear", "isolation"),
                ("shoulders", "rear", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("abs", "abs", "isolation")]

    },

    "legs": {

        "30": [("legs", "legs", "compound"),
               ("legs", random.choice(legs_muscles_list), "compound"),
               ("legs", random.choice(legs_muscles_list), "compound")],

        "45": [("legs", "legs", "compound"),
               ("legs", "quads", "compound"),
               ("legs", "hamstrings", "compound"),
               ("legs", "calves", "isolation")
               ],

        "60":  [("legs", "legs", "compound"),
                ("legs", "glutes", "compound"),
                ("legs", "quads", "compound"),
                ("legs", "hamstrings", "compound"),
                ("legs", "calves", "isolation")
                ],

        "75": [("legs", "legs", "compound"),
               ("legs", random.choice(legs_muscles_list), "compound"),
               ("legs", "glutes", "compound"),
               ("legs", "quads", "compound"),
               ("legs", "hamstrings", "isolation"),
               ("legs", "calves", "isolation")
               ],

        "90": [("legs", "legs", "compound"),
               ("legs", random.choice(legs_muscles_list), "compound"),
               ("legs", "glutes", "compound"),
               ("legs", "quads", "isolation"),
               ("legs", "hamstrings", "isolation"),
               ("legs", "calves", "isolation"),
               ("abs", "abs", "isolation")
               ],

        "105": [("legs", "legs", "compound"),
                ("legs", random.choice(legs_muscles_list), "compound"),
                ("legs", "glutes", "compound"),
                ("legs", random.choice(legs_muscles_list), "compound"),
                ("legs", "quads", "isolation"),
                ("legs", "hamstrings", "isolation"),
                ("legs", "calves", "isolation"),
                ("abs", "abs", "isolation")
                ],

        "120": [("legs", "legs", "compound"),
                ("legs", random.choice(legs_muscles_list), "compound"),
                ("legs", "glutes", "compound"),
                ("legs", "quads", "compound"),
                ("legs", "hamstrings", "compound"),
                ("legs", random.choice(legs_muscles_list), "isolation"),
                ("legs", random.choice(legs_muscles_list), "isolation"),
                ("legs", "calves", "isolation"),
                ("abs", "abs", "isolation")
                ]

    },

    "upper": {

        "30": [("chest", "chest", "compound"),
               ("back", "mid-back", "compound"),
               ("shoulders", "shoulders", "compound")],


        "45": [("chest", "chest", "compound"),
               ("back", "mid-back", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("abs", "abs", "isolation")],

        "60": [("chest", "chest", "compound"),
               ("back", "mid-back", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("chest", "chest", "compound"),
               ("back", "lats", "compound"),
               ("abs", "abs", "isolation")],

        "75": [("chest", "chest", "compound"),
               ("back", "mid-back", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("chest", "chest", "compound"),
               ("back", "lats", "compound"),
               ("arms", "biceps", "compound"),
               ("abs", "abs", "isolation")],

        "90": [("chest", "chest", "compound"),
               ("back", "mid-back", "compound"),
               ("shoulders", "shoulders", "compound"),
               ("chest", "chest", "compound"),
               ("back", "lats", "compound"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("abs", "abs", "isolation")],

        "105": [("chest", "chest", "compound"),
                ("back", "mid-back", "compound"),
                ("shoulders", "shoulders", "compound"),
                ("chest", "chest", "compound"),
                ("back", "lats", "compound"),
                ("arms", "biceps", "isolaton"),
                ("arms", "triceps", "isolation"),
                ("shoulders", "rear", "isolation"),
                ("abs", "abs", "isolation")],

        "120": [("chest", "chest", "compound"),
                ("back", "mid-back", "compound"),
                ("shoulders", "shoulders", "compound"),
                ("chest", "chest", "compound"),
                ("back", "lats", "compound"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("shoulders", "rear", "isolation"),
                ("abs", "abs", "isolation"),
                ("abs", "abs", "isolation")
                ]

    },

    "chest": {

        "30": [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", random.choice(chest_muscles_list), "compound")],

        "45": [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", random.choice(chest_muscles_list), "compound"),
               ("chest", random.choice(chest_muscles_list), "isolation")],

        "60": [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", random.choice(chest_muscles_list), "isolation")],

        "75": [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "lower-chest", "compound"),
               ("chest", random.choice(chest_muscles_list), "isolation")],

        "90": [("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "chest", "compound"),
               ("chest", "upper-chest", "compound"),
               ("chest", "lower-chest", "compound"),
               ("chest", "chest", "isolation"),
               ("chest", random.choice(chest_muscles_list), "isolation")],

        "105": [("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "lower-chest", "compound"),
                ("chest", "chest", "isolation"),
                ("chest", "upper-chest", "isolation"),
                ("chest", random.choice(chest_muscles_list), "isolation")],

        "120": [("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "chest", "compound"),
                ("chest", "upper-chest", "compound"),
                ("chest", "lower-chest", "compound"),
                ("chest", "chest", "isolation"),
                ("chest", "upper-chest", "isolation"),
                ("chest", "upper-chest", "isolation"),
                ("chest", random.choice(chest_muscles_list), "isolation")]

    },

    "back": {

        "30": [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound")],

        "45": [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", random.choice(back_muscles_list), "isolation")],


        "60": [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", "upper-back", "compound"),
               ("back", random.choice(back_muscles_list), "isolation")],

        "75": [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lower-back", "isolation"),
               ("back", random.choice(back_muscles_list), "isolation")],

        "90": [("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", "mid-back", "compound"),
               ("back", "upper-back", "compound"),
               ("back", "lats", "compound"),
               ("back", "lower-back", "isolation")],

        "105": [("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", random.choice(back_muscles_list), "isolation"),
                ("back", random.choice(back_muscles_list), "isolation")],

        "120": [("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", "mid-back", "compound"),
                ("back", "upper-back", "compound"),
                ("back", "lats", "compound"),
                ("back", "mid-back", "isolation"),
                ("back", "upper-back", "isolation"),
                ("back", "lats", "isolation")]

    },

    "arms": {

        "30": [("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation")
               ],

        "45": [("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation")
               ],

        "60": [("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation")
               ],

        "75": [("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation")
               ],

        "90": [("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation"),
               ("arms", "triceps", "isolation"),
               ("arms", "biceps", "isolation")
               ],

        "105": [("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation")
                ],

        "120": [("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation"),
                ("arms", "triceps", "isolation"),
                ("arms", "biceps", "isolation")
                ]

    },

    "shoulders": {

        "30": [("shoulder", "shoulder", "compound"),
               ("shoulder", "shoulder", "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "isolation")
               ],


        "45": [("shoulder", "shoulder", "compound"),
               ("shoulder", "shoulder", "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "isolation"),
               ("shoulder", "rear", "isolation")
               ],


        "60": [("shoulder", "shoulder", "compound"),
               ("shoulder", "shoulder", "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "isolation"),
               ("shoulder", "rear", "isolation")
               ],

        "75": [("shoulder", "shoulder", "compound"),
               ("shoulder", "shoulder", "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "isolation"),
               ("shoulder", "rear", "isolation"),
               ("shoulder", "lateral", "isolation")
               ],

        "90": [("shoulder", "shoulder", "compound"),
               ("shoulder", "shoulder", "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "compound"),
               ("shoulder", random.choice(
                   shoulder_muscle_list), "compound"),
               ("shoulder", "rear", "isolation"),
               ("shoulder", "lateral", "isolation"),
               ("shoulder", "rear", "isolation")
               ],

        "105": [("shoulder", "shoulder", "compound"),
                ("shoulder", "shoulder", "compound"),
                ("shoulder", random.choice(
                    shoulder_muscle_list), "compound"),
                ("shoulder", random.choice(
                    shoulder_muscle_list), "compound"),
                ("shoulder", "rear", "isolation"),
                ("shoulder", "lateral", "isolation"),
                ("shoulder", "anterior", "isolation"),
                ("shoulder", "rear", "isolation")
                ],

        "120": [("shoulder", "shoulder", "compound"),
                ("shoulder", "shoulder", "compound"),
                ("shoulder", random.choice(
                    shoulder_muscle_list), "compound"),
                ("shoulder", random.choice(
                    shoulder_muscle_list), "compound"),
                ("shoulder", random.choice(
                    shoulder_muscle_list), "compound"),
                ("shoulder", "rear", "isolation"),
                ("shoulder", "lateral", "isolation"),
                ("shoulder", "anterior", "isolation"),
                ("shoulder", "rear", "isolation")
                ]

    }

}
