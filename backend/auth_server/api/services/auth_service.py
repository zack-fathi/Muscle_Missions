"""Authentication Service - Handles user authentication and account management."""

import uuid
import hashlib
import re
from flask import jsonify, request, make_response
from model import get_db
from utils import check_logname_exists

def login_user(data):
    """Handles user login."""
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    connection = get_db()
    user = check_user_exists(connection, username)

    if not user:
        return jsonify({"error": "Invalid username or password"}), 401

    password_db_string = get_hashed_password(password, user["password"])
    if password_db_string != user["password"]:
        return jsonify({"error": "Invalid username or password"}), 401

    resp = make_response(jsonify({"message": "Login successful"}), 200)
    resp.set_cookie('username', username)
    return resp

def create_user(data):
    """Handles account creation."""
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing required fields"}), 400

    if not validate_password(password):
        return jsonify({"error": "Password must contain at least one number, one uppercase and lowercase letter, and at least 8 or more characters"}), 400

    hashed_password = hash_password(password)
    connection = get_db()

    try:
        connection.execute("INSERT INTO users (username, password, age) VALUES (?, ?, ?)", (username, hashed_password, -1))
        connection.commit()
        return jsonify({"message": "Account created successfully"}), 201
    except Exception:
        return jsonify({"error": "Username already exists"}), 400

def edit_user_password(data):
    """Handles password changes."""
    username = request.cookies.get('username')
    old_password = data.get('password')
    new_password = data.get('new_password')

    if not username or not old_password or not new_password:
        return jsonify({"error": "Missing required fields"}), 400

    connection = get_db()
    user = check_user_exists(connection, username)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if get_hashed_password(old_password, user['password']) != user['password']:
        return jsonify({"error": "Incorrect password"}), 403

    if not validate_password(new_password):
        return jsonify({"error": "Password does not meet security requirements"}), 400

    new_hashed_password = hash_password(new_password)
    connection.execute("UPDATE users SET password = ? WHERE username = ?", (new_hashed_password, username))
    connection.commit()
    
    return jsonify({"message": "Password updated successfully"}), 200

def update_user_info(data):
    """Updates additional user details."""
    username = request.cookies.get('username')
    
    if not username:
        return jsonify({"error": "Unauthorized"}), 401

    age = data.get('age')
    height = data.get('height')
    weight = data.get('weight')
    activity_level = data.get('activity_level')
    experience = data.get('experience')
    gender = data.get('gender')

    connection = get_db()
    connection.execute(
        "UPDATE users SET age = ?, height = ?, weight = ?, fitness_level = ?, workout_experience = ?, gender = ? WHERE username = ?",
        (age, height, weight, activity_level, experience, gender, username)
    )
    connection.commit()

    return jsonify({"message": "User info updated successfully"}), 200

def authenticate_user():
    """Checks if user is logged in."""
    if not check_logname_exists():
        return jsonify({"logged_in": False, "message": "No user logged in"}), 200
    return jsonify({"logged_in": True, "message": "User is authenticated"}), 200

def hash_password(password):
    """Hashes password using SHA-512 with a salt."""
    algorithm = 'sha512'
    salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    hash_obj.update((salt + password).encode('utf-8'))
    return "$".join([algorithm, salt, hash_obj.hexdigest()])

def get_hashed_password(password, db_password):
    """Hashes user input using stored salt for verification."""
    algorithm, salt, _ = db_password.split("$")
    hash_obj = hashlib.new(algorithm)
    hash_obj.update((salt + password).encode('utf-8'))
    return "$".join([algorithm, salt, hash_obj.hexdigest()])

def check_user_exists(connection, username):
    """Check if a user exists in the database."""
    cur = connection.execute("SELECT username, password FROM users WHERE username = ?", (username,))
    return cur.fetchone()

def validate_password(password):
    """Validates password strength."""
    return bool(re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', password))
