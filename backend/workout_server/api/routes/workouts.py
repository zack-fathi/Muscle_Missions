"""Workout API Routes."""

from flask import Blueprint, request, jsonify
from workout_server.api.services import register_services

# Register services dynamically
services = register_services()

# Define Blueprint
workouts_bp = Blueprint("workouts", __name__, url_prefix="/api/workouts")

@workouts_bp.route('/day/', methods=['POST'])
def generate_daily():
    """Generate a daily workout."""
    form_data = request.get_json()
    return services["workouts"]["generate_workout_plan"](form_data, is_split=False)

@workouts_bp.route('/split/', methods=['POST'])
def generate_split():
    """Generate a multi-day workout split."""
    form_data = request.get_json()
    return services["workouts"]["generate_workout_plan"](form_data, is_split=True)

@workouts_bp.route('/save/', methods=['POST'])
def save():
    """Save a workout."""
    form_data = request.get_json()
    return services["workouts"]["save_workout"](form_data)

@workouts_bp.route('/last_saved/', methods=['GET'])
def get_last_saved():
    """Retrieve the last saved workout from the database."""
    return services["workouts"]["get_last_saved_workout"]()

__all__ = ["workouts_bp"]

