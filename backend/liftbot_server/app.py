import os
from flask import Flask
from flask_cors import CORS
from api.routes import liftbot_bp
from config import config  # This comes from your get_config() function
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask App
app = Flask(__name__)
app.config.from_object(config)

# Enable CORS using the origins and support settings from the config
CORS(app, resources={r"/api/*": {"origins": config.CORS_ORIGINS}}, 
     supports_credentials=config.CORS_SUPPORTS_CREDENTIALS)

# Register API Routes
app.register_blueprint(liftbot_bp)

if __name__ == "__main__":
    # Determine the environment (defaults to development)
    env = os.getenv("APP_ENV", "development").lower()

    # In production, bind to all network interfaces; otherwise, use localhost.
    host = "0.0.0.0" if env == "production" else "127.0.0.1"

    # Get the port from an environment variable or default to 5003.
    port = int(os.getenv("PORT", 5003))
    
    print(f"Starting app in {env} mode on {host}:{port}")
    app.run(host=host, port=port, debug=config.DEBUG)
