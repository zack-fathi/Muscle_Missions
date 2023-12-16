"""Account creation view."""

import os
import uuid
import hashlib
import pathlib
import flask
import muscle

@muscle.app.route('/accounts/login/')
def show_login():
    """Show the login page for a user."""

    return flask.send_from_directory("static/html","login.html")

@muscle.app.route('/accounts/create/')
def show_create():
    """Show the account creation page."""

    return flask.send_from_directory("static/html", "create.html")

@muscle.app.route('/accounts/edit/')
def show_edit():
    """Shows edit password."""

    return flask.send_from_directory("static/html","edit.html")

@muscle.app.route('/accounts/auth/')
def auth():
    """Authenticate a user."""
    logname = flask.request.cookies.get('username', -1)
    if logname == -1:
        flask.abort(403)
    return flask.make_response("", 200)

@muscle.app.route('/accounts/', methods = ['POST'])
def handle_submit():
    """Handle submit info."""
    connection = muscle.model.get_db()
    print("Connection is ", connection)

    form = flask.request.form.to_dict()
    operation = form['operation']

    if operation == "login":
        return login_help(connection, form)
    if operation == "create":
        test_db_connection()
        return create_help(connection, form)
    if operation == "edit":
        return edit_help(connection, form)
    if operation == "delete":
        return 'delete'
    return None
    
def login_help(connection, form):
    """Login help function."""

    username = form['username']
    password = form['password']

    user = check_user_exists(connection, username, password)

    # hash and salt according to user password
    password_db_string = get_hashed_password(password, user['password'])

    if password_db_string == user["password"]:
        resp = flask.make_response(flask.redirect("/", 302))
        resp.set_cookie('username', username)
        return resp
        
    flask.abort(403)

def create_help(connection, form):
    """Account creation submit form."""

    name = form["fullname"]
    username = form['username']
    password = form['password']

    # check if account exits
    cur = connection.execute(
        "SELECT username, password "
        "FROM users "
        "WHERE username == ?",
        (username, )
    )

    user = cur.fetchall()

    if user:
        flask.abort(403)

    hashed_password = hash_password(password)
    
    cur = connection.execute(
        "INSERT INTO users(username, password) "
        "VALUES (?, ?)",
        (username, hashed_password)
    )
    
    connection.commit()

    resp = flask.make_response(flask.redirect("/", 302))
    resp.set_cookie('username', username)
    return resp

def edit_help(connection, form):
    """Help with editing password."""

    login_name = flask.request.cookies.get('username', -1)
    if login_name == -1:
        flask.abort(403)
    
    password = form['password']
    new_password = form['new']
    new_password2 = form['new2']

    if new_password == "" or new_password2 == "":
        flask.abort(400)

    if new_password != new_password2:
        flask.abort(401)

    user = check_user_exists(connection,login_name, password)
    password_db_string = get_hashed_password(password, user['password'])

    if password_db_string == user['password']:
        new_password = hash_password(new_password)
        edit_password(connection,login_name,new_password)

    return flask.redirect(flask.request.args.get("target"),302)


def edit_password(connection, username, new_password):
    """Change the password."""

    cur = connection.execute(
        "UPDATE users "
        "SET password = ? "
        "WHERE username == ? ",
        (new_password, username,)
    )
    

def hash_password(password):
    """Hash a password."""

    # hash and salt
    algorithm = 'sha512'
    salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_db_string = salt + password
    hash_obj.update(password_db_string.encode('utf-8'))
    password_db_string = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_db_string])
    return password_db_string

def get_hashed_password(password, db_password):
    """Hashes user input according to db salt."""

    algorithm = 'sha512'
    salt = db_password.split("$")
    salt = salt[1]
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string

def check_user_exists(connection, username, password):
    """Check if a user exists."""

    cur = connection.execute(
        "SELECT username, password "
        "FROM users "
        "WHERE username == ?",
        (username,)
    )

    user = cur.fetchone()

    if username == "" or password == "":
        flask.abort(400)

    print("user is " , user)
    if user is None:
        flask.abort(403)

    return user

def test_db_connection():
    try:
        connection = muscle.model.get_db()
        cur = connection.execute("SELECT 1")
        result = cur.fetchone()
        print("Database connection test result:", result)
        return True
    except Exception as e:
        print("Error testing database connection:", e)
        return False
