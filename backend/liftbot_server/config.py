import os
from dotenv import load_dotenv

# Load environment variables from .env file (must be called before using os.getenv)
load_dotenv()

class BaseConfig:
    """Base configuration for the Muscle Missions authentication server using SQLite3."""
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    print("BASE_DIR:", BASE_DIR)

    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False  # Default is False; override in child classes as needed

    # CORS configuration
    CORS_ORIGINS = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:3000,http://localhost:5001,http://localhost:5002"
    ).split(",")
    CORS_SUPPORTS_CREDENTIALS = True

    # Cookie security settings
    COOKIE_HTTPONLY = True
    COOKIE_SAMESITE = "None"
    COOKIE_SECURE = os.getenv("COOKIE_SECURE", "False").lower() in ("true", "1", "yes")

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True

class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False

def get_config():
    """
    Retrieve the configuration class based on the APP_ENV environment variable.
    Defaults to DevelopmentConfig if not set.
    """
    env = os.getenv("APP_ENV", "development").lower()
    if env == "production":
        return ProductionConfig
    elif env == "testing":
        return TestingConfig
    else:
        return DevelopmentConfig

# For convenience, you can import 'config' in your application
config = get_config()
