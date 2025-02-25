#!/bin/sh
# entrypoint.sh

set -e

echo "Starting Exercises database..."
./scripts/exercisesdb.sh create exercises &

sleep 5

if [ "$APP_ENV" = "development" ]; then
  echo "Starting Flask development server..."
  # Optionally, enable reloading with the --reload flag if you want auto-restart on code changes
  exec python app.py
else
  echo "Starting Gunicorn server..."
  exec gunicorn --bind "0.0.0.0:5001" app:app
fi
