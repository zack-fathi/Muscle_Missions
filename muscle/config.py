"""Config file."""
import pathlib

# File Upload to var/uploads/
SEARCH_ROOT = pathlib.Path(__file__).resolve().parent.parent

DATABASE_FILENAME = SEARCH_ROOT/'var'/'muscle.sqlite3'
