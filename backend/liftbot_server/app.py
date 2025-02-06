"""Authentication Server - Handles user authentication and account management."""

import sys
import os

# Ensure backend directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask
from flask_cors import CORS
from liftbot_server.api.routes import liftbot_bp
from model import get_db, close_db

# Initialize Flask App
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "http://localhost:5001", "http://localhost:5002"]}}, supports_credentials=True)

# Register API Routes
app.register_blueprint(liftbot_bp)
app.secret_key = os.getenv("SECRET_KEY")


@app.teardown_appcontext
def teardown_db(error):
    """Close the database connection at the end of the request."""
    close_db(error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
