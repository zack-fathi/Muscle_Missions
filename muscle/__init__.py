"""Initial server configuration."""

from flask import Flask
from flask_session import Session
from flask_cors import CORS
from config import Config  
from model import close_db

# Initialize Flask App
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing)
CORS(app, supports_credentials=True)

# Load Configuration
app.config.from_object(Config)

# Session Configuration
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
Session(app)

# Ensure Database Closes at End of Request
@app.teardown_appcontext
def teardown_db(error):
    """Close the database connection at the end of the request."""
    close_db(error)

# Import and Register API Blueprints
from muscle.api.routes import accounts_bp, workouts_bp, liftbot_bp  
app.register_blueprint(accounts_bp)
app.register_blueprint(workouts_bp)
app.register_blueprint(liftbot_bp)

# Import Other Modules
import muscle.model  