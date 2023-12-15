"""Initialization for server."""

import os
from flask import Flask

app = Flask(__name__)
app.config.from_object('muscle.config')

import muscle.model
import muscle.views
