"""Initialize API route Blueprints."""

# Import blueprints from individual route modules
from .accounts import accounts_bp
from ....workout_server.api.routes.workouts import workouts_bp
from .liftbot import liftbot_bp

# Expose blueprints for easy imports in `api/__init__.py`
__all__ = ["accounts_bp", "workouts_bp", "liftbot_bp"]
