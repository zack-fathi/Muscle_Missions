"""User Account API Routes."""

from flask import Blueprint, request, jsonify
from muscle.api.services import register_services

# Register services dynamically
services = register_services()

# Define Blueprint
accounts_bp = Blueprint("accounts", __name__, url_prefix="/api/accounts")

@accounts_bp.route('/login/', methods=['POST'])
def login():
    """Handle user login."""
    return services["auth"]["login_user"](request.get_json())

@accounts_bp.route('/create/', methods=['POST'])
def create_account():
    """Handle new account creation."""
    return services["auth"]["create_user"](request.get_json())

@accounts_bp.route('/edit_password/', methods=['POST'])
def edit_password():
    """Change user password."""
    return services["auth"]["edit_user_password"](request.get_json())

@accounts_bp.route('/edit_more_info/', methods=['POST'])
def edit_more_info():
    """Edit additional user information."""
    return services["auth"]["update_user_info"](request.get_json())

@accounts_bp.route('/auth/', methods=['GET'])
def auth():
    """Authenticate user session."""
    return services["auth"]["authenticate_user"]()
