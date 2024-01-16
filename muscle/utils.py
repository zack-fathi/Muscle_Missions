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
    flask.session.clear()
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

def get_user_information():
    """Get the user information."""
    
    user_info = {}
    connection = muscle.model.get_db()
    logname = flask.request.cookies.get('username')

    cur = connection.execute(
        "SELECT * FROM users "
        "WHERE username = ? ",
        (logname,)
    ).fetchone()

    if cur is None:
        print("User not found")
        return None

    return cur

def get_last_split_workout(connection, split_id):
    """Show the workout split."""

    split_workouts = connection.execute(
        "SELECT * FROM workouts WHERE splitID = ? ",
        (split_id,)
    ).fetchall()

    combined_workout = []
    for workout in split_workouts:
        exercises = connection.execute(
            "SELECT e.name, we.sets, we.reps FROM workout_exercises we JOIN exercises e ON we.exerciseID = e.exerciseID WHERE we.workoutID = ? ",
            (workout["workoutID"],)
        ).fetchall()
        combined_workout.append(exercises)

    return combined_workout

def get_last_single_workout(connection, workoutID):
    """Show the workout."""
    workout_exercises = connection.execute(
        "SELECT e.name, we.sets, we.reps FROM workout_exercises we JOIN exercises e ON we.exerciseID = e.exerciseID WHERE we.workoutID = ?",
        (workoutID,)
    ).fetchall()
    return workout_exercises

def check_user_settings():
    """Sees if a user has filled out the additional data needed."""
    connection = muscle.model.get_db()
    logname = flask.request.cookies.get('username', None)

    cur = connection.execute(
        "SELECT age from users "
        "WHERE username == ? ",
        (logname,)
    )
    
    return cur.fetchone()

def do_background_check():
    """Background check which prevents users from accessing content they cannot."""
    if 'redirected' in flask.session:
        # Clear the session variable and proceed without redirecting
        del flask.session['redirected']
        return

    if not check_logname_exists():
        flask.session['redirected'] = True
        return flask.redirect("/accounts/login/", 302)
    
    if check_user_settings()['age'] == -1:
        flask.session['redirected'] = True
        return flask.redirect("/accounts/more_info/", 302)


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

activity_map = {

    "na":"sedentary (0-2 hours per week of activity)",
    "la":"lightly active (2-3 hours per week of activity)",
    "ma":"moderately active (3-5 hours per week of activity)",
    "va":"very active (5+ days per week of activity)"
}

workout_experience_map = {
    0: "beginner (0-1 years experience)",
    1: "intermediate (1-3 years experience)",
    2: "advanced (3+ years experience)"
}

plank_map = {

    0: 30,
    1: 60,
    2: 90
}