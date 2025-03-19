# auth_server/tests/conftest.py
import pytest
from flask import Flask
from api.routes import accounts_bp

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "test_secret"
    # Register the blueprint we want to test
    app.register_blueprint(accounts_bp)

    return app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
