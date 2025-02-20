#!/bin/bash
set -Eeuo pipefail

# --------------------------------------------------
# 1) Parse Arguments
# --------------------------------------------------
if [ $# -lt 2 ]; then
    echo "Usage: $0 {create|destroy|reset} <DB_NAME>"
    echo "Example: $0 create exercises"
    exit 1
fi

ACTION="$1"
DB_NAME="$2"

# Map the provided name to /app/var/<DB_NAME>.sqlite3
DB_FILE="/app/var/${DB_NAME}.sqlite3"

# --------------------------------------------------
# 2) Define paths to SQL files
# --------------------------------------------------
SCHEMA_SCRIPT="/app/sql/schema.sql"
DATA_SCRIPT="/app/sql/data.sql"

# Ensure /app/var exists
mkdir -p /app/var

# Check for SQL files
if [[ ! -f "$SCHEMA_SCRIPT" || ! -f "$DATA_SCRIPT" ]]; then
    echo "❌ ERROR: Missing schema or data SQL file!"
    echo "Looking for:"
    echo "  - $SCHEMA_SCRIPT"
    echo "  - $DATA_SCRIPT"
    exit 1
fi

# --------------------------------------------------
# 3) Define Functions
# --------------------------------------------------
create_db() {
    if [ -f "$DB_FILE" ]; then
        echo "⚠️ ERROR: Database already exists at $DB_FILE!"
        exit 1
    fi
    echo "✅ Creating database at $DB_FILE..."

    python3 - <<EOF
import sqlite3
with sqlite3.connect("$DB_FILE") as conn:
    with open("$SCHEMA_SCRIPT", "r") as f:
        conn.executescript(f.read())
    with open("$DATA_SCRIPT", "r") as f:
        conn.executescript(f.read())
print("🎉 Database created successfully at $DB_FILE")
EOF
}

destroy_db() {
    if [ -f "$DB_FILE" ]; then
        echo "⚠️ Destroying database at $DB_FILE..."
        rm -f "$DB_FILE"
        echo "✅ Database removed!"
    else
        echo "⚠️ No database found at $DB_FILE!"
    fi
}

reset_db() {
    destroy_db
    create_db
}

# --------------------------------------------------
# 4) Dispatch Based on ACTION
# --------------------------------------------------
case "$ACTION" in
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
        echo "⚠️ Invalid option: $ACTION"
        echo "Usage: $0 {create|destroy|reset} <DB_NAME>"
        exit 1
        ;;
esac
