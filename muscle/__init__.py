"""Initialization for server."""

from flask import Flask
from .config import Config
import os

print("Current directory:", os.getcwd())
app = Flask(__name__)
app.config.from_object(Config)


# Import other views
from muscle import views
from muscle import model
