"""Index page."""

import os
import uuid
import hashlib
import pathlib
import flask
import muscle

@muscle.app.route('/')
def show_index():
    """Main page."""
    connection = muscle.model.get_db()

    logname = flask.request.cookies.get('username', -1)

    if logname == -1:
        return flask.redirect("accounts/login/", 302)
    
    return flask.send_from_directory("static/html", "index.html")