#!/bin/bash
# exercisesdb.sh
# This script provides options to create, destroy, or reset the SQLite database
# using the provided schema (schema.sql) and data (data.sql) files.
#
# Usage:
#   ./exercisesdb.sh {create|destroy|reset}
#
# Requirements:
# - SQLite3 must be installed.
# - The script assumes the following structure relative to its own location:
#       ../backend/var         -> Database directory
#       ../backend/sql/schema.sql  -> SQL file to create the schema
#       ../backend/sql/data.sql    -> SQL file to load sample data

set -Eeuo pipefail

# Detect the appropriate realpath command (GNU or BSD)
if command -v grealpath >/dev/null 2>&1; then
    REALPATH="grealpath"
else
    REALPATH="realpath"
fi

# Get the absolute path of the script directory
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

# Define paths relative to the project root
DB_DIR="$($REALPATH "${SCRIPT_DIR}/../var/")"
DB_FILE="${DB_DIR}/exercises.sqlite3"
SCHEMA_SCRIPT="$($REALPATH "${SCRIPT_DIR}/../sql/schema.sql")"
DATA_SCRIPT="$($REALPATH "${SCRIPT_DIR}/../sql/data.sql")"

echo "DB_FILE: ${DB_FILE}"

# Function to validate that the SQL files exist
validate_paths() {
    if [ ! -f "${SCHEMA_SCRIPT}" ]; then
        echo "❌ ERROR: Schema file not found: ${SCHEMA_SCRIPT}"
        exit 1
    fi
    if [ ! -f "${DATA_SCRIPT}" ]; then
        echo "❌ ERROR: Data file not found: ${DATA_SCRIPT}"
        exit 1
    fi
}

# Function to create the database
create_db() {
    if [ -f "${DB_FILE}" ]; then
        echo "⚠️  ERROR: Database already exists!"
        exit 1
    fi
    echo "✅ Creating database..."
    mkdir -p "${DB_DIR}"
    validate_paths
    sqlite3 "${DB_FILE}" < "${SCHEMA_SCRIPT}"
    sqlite3 "${DB_FILE}" < "${DATA_SCRIPT}"
    echo "🎉 Database created successfully at ${DB_FILE}"
}

# Function to destroy the database
destroy_db() {
    if [ -f "${DB_FILE}" ]; then
        echo "⚠️  Destroying database..."
        rm -f "${DB_FILE}"
        echo "✅ Database removed!"
    else
        echo "⚠️  No database found at ${DB_FILE}"
    fi
}

# Function to reset the database (destroy then create)
reset_db() {
    echo "⚠️  Resetting database..."
    rm -f "${DB_FILE}" || true
    mkdir -p "${DB_DIR}"
    validate_paths
    sqlite3 "${DB_FILE}" < "${SCHEMA_SCRIPT}"
    sqlite3 "${DB_FILE}" < "${DATA_SCRIPT}"
    echo "✅ Database reset successfully at ${DB_FILE}!"
}

# Check that exactly one argument was provided
if [ "$#" -ne 1 ]; then
    echo "⚠️  Usage: $0 {create|destroy|reset}"
    exit 1
fi

# Process the command-line argument
case "$1" in
    create)
        create_db
        ;;
    destroy)
        destroy_db
        ;;
    reset)
        reset_db
        ;;
    *)
        echo "⚠️  Invalid option. Usage: $0 {create|destroy|reset}"
        exit 1
        ;;
esac
