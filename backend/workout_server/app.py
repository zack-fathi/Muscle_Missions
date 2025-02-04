"""Entry point for the Workout Server."""

import sys
import os

# Add backend directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__))) 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  

from flask import Flask
from flask_cors import CORS
from workout_server.api.routes import workouts_bp 

# Initialize Flask App
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "http://localhost:5002"]}}, supports_credentials=True)
# Register API Routes
app.register_blueprint(workouts_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
