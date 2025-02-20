"""Database API for Muscle Missions."""
import sqlite3
import flask
from config import Config

def dict_factory(cursor, row):
    """Convert database row objects to a dictionary keyed on column name."""
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

def get_db():
    """Open a new SQLite database connection if not already established."""
    if "sqlite_db" not in flask.g:
        flask.g.sqlite_db = sqlite3.connect(
            str(Config.DATABASE_FILENAME), 
            check_same_thread=False  # Prevent threading issues
        )
        flask.g.sqlite_db.row_factory = dict_factory
        flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")  # Ensure foreign keys are enabled
    return flask.g.sqlite_db

def close_db(error=None):
    """Close the database connection at the end of a request."""
    db = flask.g.pop("sqlite_db", None)
    if db:
        db.commit()
        db.close()
