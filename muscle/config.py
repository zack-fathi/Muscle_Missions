"""Config file."""
import pathlib

APPLICATION_ROOT = '/'

# File Upload to var/uploads/
ROOT = pathlib.Path(__file__).resolve().parent.parent

DATABASE_FILENAME = ROOT/'var'/'muscle.sqlite3'