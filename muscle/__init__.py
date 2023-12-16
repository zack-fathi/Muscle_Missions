"""Initialization for server."""

# import os
# from flask import Flask

# app = Flask(__name__)
# app.config.from_object('muscle.config')

# from flask import Flask
# from muscle.views import index_bp  # Import the Blueprint from your views package

# app = Flask(__name__)
# app.config.from_object('muscle.config')  # Load configuration

# # Register the blueprints with the Flask application
# app.register_blueprint(index_bp)

from flask import Flask, send_from_directory

app = Flask(__name__)
app.config.from_object('muscle.config')

# Import other views
from muscle import views
from muscle import model
