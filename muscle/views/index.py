"""Index page."""

import os
import uuid
import hashlib
import pathlib
import flask
import muscle
from .. import utils


@muscle.app.route('/')
def show_index():
    """Main page."""
    connection = muscle.model.get_db()

    logname = flask.request.cookies.get('username', None)

    # this might be redundant
    if not logname or not check_for_user(connection, logname):
        return utils.clear_cookie()

    # check if user hasn't inputted new information
    if utils.check_user_settings()['age'] == -1:
        return flask.redirect("/accounts/more_info/", 302)

    context = {"logname": logname}
    return flask.render_template("index.html", **context)


def check_for_user(connection, logname):
    """Used for initial entry """

    cur = connection.execute(
        "SELECT username "
        "FROM users "
        "WHERE username == ?",
        (logname,)
    )

    return cur.fetchone() is not None
