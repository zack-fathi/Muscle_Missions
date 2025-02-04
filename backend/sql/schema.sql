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

CREATE TABLE workouts (
    workoutID INTEGER PRIMARY KEY AUTOINCREMENT,
    splitID INTEGER, -- Links this workout to a specific split
    userID INTEGER NOT NULL,
    workoutType TEXT NOT NULL,
    workout_number INTEGER NOT NULL, -- The order of the workout within the split
    duration INTEGER NOT NULL, -- Duration in minutes
    difficulty TEXT NOT NULL,
    FOREIGN KEY (userID) REFERENCES users(userID) ON DELETE CASCADE,
    FOREIGN KEY (splitID) REFERENCES workout_splits(splitID) ON DELETE CASCADE
);

CREATE TABLE workout_exercises (
    workoutExerciseID INTEGER PRIMARY KEY AUTOINCREMENT,
    workoutID INTEGER NOT NULL,
    exerciseID INTEGER NOT NULL,
    orderInWorkout INTEGER NOT NULL,
    sets INTEGER NOT NULL,
    reps INTEGER NOT NULL,
    FOREIGN KEY (workoutID) REFERENCES workouts(workoutID) ON DELETE CASCADE,
    FOREIGN KEY (exerciseID) REFERENCES exercises(exerciseID)
);

CREATE TABLE workout_splits (
    splitID INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER NOT NULL,
    splitType TEXT , -- e.g., '3-Day Split', 'Full Body', etc.
    splitDescription TEXT, -- Optional, a description of the split
    FOREIGN KEY (userID) REFERENCES users(userID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS saved_workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER,
    workout_data TEXT
);
