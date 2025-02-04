"""Initialize API routes for the Muscle Missions backend."""

from flask import Blueprint

# Create main API Blueprint
api = Blueprint("api", __name__, url_prefix="/api")

# Import and register submodules from `routes/__init__.py`
from muscle.api.routes import accounts_bp, workouts_bp, liftbot_bp

# Register API blueprints
api.register_blueprint(accounts_bp)
api.register_blueprint(workouts_bp)
api.register_blueprint(liftbot_bp)
