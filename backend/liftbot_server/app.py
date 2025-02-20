import sys
import os


from flask import Flask
from flask_cors import CORS
from api.routes import liftbot_bp
from config import Config

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize Flask App
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS
CORS(app, resources={r"/api/*": {"origins": Config.CORS_ORIGINS}}, supports_credentials=Config.CORS_SUPPORTS_CREDENTIALS)

# Register API Routes
app.register_blueprint(liftbot_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=Config.DEBUG)
