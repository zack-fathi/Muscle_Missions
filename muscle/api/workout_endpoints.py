"""REST API to generate workouts."""
import flask
import muscle
import json

@muscle.app.route('api/v1/workouts/')
def get_workouts():
    """Return workout."""
    
    # Retrieve query parameters
    time = flask.request.args.get('time')
    equipment = flask.request.args.get('equipment')
    muscle_group = flask.request.args.get('muscle_group')
    fitness_level = flask.request.args.get('fitness_level')
    fitness_goals = flask.request.args.get('fitness_goals')

    workouts = fetch_workouts(time, equipment, muscle_group, fitness_level,fitness_goals)

    return jsonify(workouts)

def fetch_workouts(time, equipment, muscle_group, fitness_level,fitness_goals):
    """Fetch a wor"""