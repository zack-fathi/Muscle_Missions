#!/bin/sh
# entrypoint.sh

set -e

echo "Starting Users database..."
./scripts/usersdb.sh create users &

sleep 1


if [ "$APP_ENV" = "development" ]; then
  echo "Starting Flask development server..."
  # Optionally, enable reloading with the --reload flag if you want auto-restart on code changes
  exec python app.py
else
  echo "Starting Gunicorn server..."
  exec gunicorn --bind "0.0.0.0:5002" app:app
fi
