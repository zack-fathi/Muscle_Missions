"""Liftbot API Routes."""

from flask import Blueprint, request
from muscle.api.services import register_services

# Register services dynamically
services = register_services()

# Define Blueprint
liftbot_bp = Blueprint("liftbot", __name__, url_prefix="/api/liftbot")

@liftbot_bp.route("/", methods=["GET"])
def show_liftbot():
    """Show the liftbot screen."""
    return services["liftbot"]["show_liftbot"]()

@liftbot_bp.route("/process_message/", methods=["POST"])
def process_message():
    """Process a message from the user."""
    return services["liftbot"]["process_message"](request.get_json())
