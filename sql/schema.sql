CREATE TABLE users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INTEGER,
    height INTEGER,
    weight INTEGER,
    fitness_level TEXT,
    workout_experience TEXT,
    gender TEXT
);
CREATE TABLE exercises (
    exerciseID INTEGER PRIMARY KEY AUTOINCREMENT,
    body_part TEXT NOT NULL,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    equipment TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    weight INTEGER
);
