import os
from dotenv import load_dotenv

# Load environment variables from .env file (must be called before os.getenv)
load_dotenv()

class Config:
    """Configuration settings for the Muscle Missions Lifbot server."""
    
    # Base directory for relative paths
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Load environment variables
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")
    
    # CORS configuration
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5001,http://localhost:5002").split(",")
    CORS_SUPPORTS_CREDENTIALS = True
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "default_openai_key")

    # Cookie security
    COOKIE_HTTPONLY = True
    COOKIE_SAMESITE = "None"
    COOKIE_SECURE = os.getenv("COOKIE_SECURE", "False").lower() in ("true", "1", "yes")
