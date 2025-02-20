import os
from dotenv import load_dotenv

# Load environment variables from .env file (must be called before os.getenv)
load_dotenv()

class Config:
    """Configuration settings for the Muscle Missions authentication server."""
    
    # Base directory for relative paths
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    print(BASE_DIR)

    # Get the database filename from the environment or default to a path within BASE_DIR.
    _db_filename = os.getenv("DATABASE_FILENAME", os.path.join(BASE_DIR, "var", "users.sqlite3"))
    
    # If the provided path is not absolute, make it absolute relative to BASE_DIR.
    if not os.path.isabs(_db_filename):
        _db_filename = os.path.join(BASE_DIR, _db_filename)
    
    print(f"Database filename: {_db_filename}")    
    DATABASE_FILENAME = _db_filename

    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")
    
    # CORS configuration
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5001,http://localhost:5003").split(",")
    CORS_SUPPORTS_CREDENTIALS = True

    # Cookie security
    COOKIE_HTTPONLY = True
    COOKIE_SAMESITE = "None"
    COOKIE_SECURE = os.getenv("COOKIE_SECURE", "False").lower() in ("true", "1", "yes")
