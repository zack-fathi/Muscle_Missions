"""Account creation view."""

import os
import uuid
import hashlib
import pathlib
import flask
import muscle

@muscle.app.route('/accounts/login')
def show_login():
    """Show the login page for a user."""
    return flask.send_from_directory("static/html","login.html")
