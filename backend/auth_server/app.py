import sys
import os


from flask import Flask
from flask_cors import CORS
from api.routes import accounts_bp
from model import get_db, close_db
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
app.register_blueprint(accounts_bp)

@app.teardown_appcontext
def teardown_db(error):
    close_db(error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=Config.DEBUG)
