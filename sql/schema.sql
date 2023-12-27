CREATE TABLE users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INTEGER,
    height INTEGER,
    weight INTEGER,
    fitness_level TEXT,
    workout_experience INTEGER,
    gender TEXT
);
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
