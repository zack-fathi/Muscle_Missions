CREATE TABLE exercises (
    exerciseID INTEGER PRIMARY KEY AUTOINCREMENT,
    muscle_group TEXT NOT NULL,
    main_muscle TEXT NOT NULL,
    movement_type TEXT NOT NULL,
    is_compound TEXT NOT NULL,
    parent_exercise TEXT NOT NULL,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    equipment TEXT NOT NULL,
    difficulty INTEGER,
    weight INTEGER
);

CREATE TABLE saved_workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    workout_data TEXT
);
