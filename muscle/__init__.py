"""Initial server configuration."""

from flask import Flask
from flask_session import Session
from flask_cors import CORS
from .config import Config

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Enable CORS
app.config.from_object(Config)

# Session Configuration
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
Session(app)

from muscle import views # noqa: E402
from muscle import model # noqa: E402
