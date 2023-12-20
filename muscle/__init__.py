"""Initialization for server."""

from flask import Flask, send_from_directory

app = Flask(__name__)
app.config.from_object('muscle.config')

# Import other views
from muscle import views
from muscle import model
from muscle import script