#!/usr/bin/env python3
import muscle

warmup_list = [
    ("Band External Shoulder Rotation", 1, "band"),
    ("Band Internal Shoulder Rotation", 1, "band"),
    ("Band Pull-Apart", 0, "band"),
    ("Banded Side Kicks", 0, "band"),
    ("Hip Abduction Against Band", 0, "band"),
    ("Hip Thrust With Band Around Knees", 0, "band"),
    ("Lateral Walk With Band", 0, "band"),
]

connection = model.get_db()

cur = connection.execute(
    "SELECT name from exercises"
)

exercises = cur.fetchall()
for exercise in exercises:
    print(exercise)
