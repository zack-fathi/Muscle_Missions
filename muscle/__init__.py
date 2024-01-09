"""Initialization for server."""

from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
print("Database Path:", Config.DATABASE_FILENAME)


# Import other views
from muscle import views
from muscle import model
