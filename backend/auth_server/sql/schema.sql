CREATE TABLE users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    fullname TEXT NOT NULL,
    password TEXT NOT NULL,
    age INTEGER,
    height INTEGER,
    weight INTEGER,
    fitness_level TEXT,
    workout_experience INTEGER NOT NULL,
);