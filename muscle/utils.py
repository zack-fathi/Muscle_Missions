"""Useful functions across all files."""

import flask
import random
import muscle


def clear_cookie():
    """Clear a cookie if removed from database."""
    response = flask.make_response(flask.redirect('/accounts/login/'))  # Redirect or return a response
    response.set_cookie('username', '', expires=0)  # Clear the cookie
    return response

# TODO: TRY TO MOVE CODE TO HERE

def check_logname_exists():
    """Check if logname exists."""

    connection = muscle.model.get_db()
    logname = flask.request.cookies.get('username', None)

    if not logname:
       return False
    
    cur = connection.execute(
        "SELECT username from users "
        "WHERE username == ? ",
        (logname,)
    )

    if not cur.fetchone:
        return False
    
    return True
    
    