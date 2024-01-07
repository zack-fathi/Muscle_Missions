# Muscle Missions

Are you bored of your workout routine and need something new in the gym? Muscle Missions can help with that! Muscle Missions is a Web App designed to create customized daily workouts, or weekly workout splits for users. Users can get custom workouts based on their workout experience, equipment access, time available, and exercise limitations. On top of that, users can also chat with an interactive chatbot that gives them tips based off their workouts, and offers additional exercise advice!

Link to project: // insert this asap

alt tag

# How It's Made:
**Tech used:** HTML, CSS, JavaScript, Python, SQLite, Flask, Bootstrap, REST, OPENAI API

**Database Design:** Muscle Missions required a very complex database design with many tables. Firstly, a users table had to be created for users. This table stores valuable information about the user such as their username, hashed and salted password, height, weight, activity level, and workout experience. I used the SHA-512 algorithm to hash the passwords to ensure security, as well as strict password constraints.  

The second table that had to be created was an exercises table. This table currently contains over 270 exercises, with many of them taken from strengthlog. Each exercise entry includes an exercise name, main muscle group (chest,legs,etc), primary muscle (quads,triceps,etc), main movement pattern, equipment needed (machine, barbell, dumbbell, etc), difficulty of the movement, and a rating (weight). The values for the weight are from 1-5, and determined based off an exercises popularity as well as its effectiveness.
The weight was very important for the selection of exercises for workout routines.
Strengthlog link: [https://www.strengthlog.com/exercise-directory/](https://www.strengthlog.com/exercise-directory/)

In order to save the users most recent workout/workout split, tables for the workout, workout split, and exercises had to be made. Each entry in the workout table includes a workout ID, and the exercises in that workout are each entries in the workout exercises table, which links to a workout via its ID. If the workout was part of a workout split, it was assigned a workout split ID and entry, and that workout split contains 2-6 workouts, each linked to the split ID. This offered an effective data retrieval method for the users last workout/workout split.

**Workout Generation:** To make the workout generation quick and effective, I created a REST API within my program that returns a workout routine with its exercises. Each type of workout (fullbody, legs, etc), has a template for each time period, which involves both a pre-planned routine, and some randomness where appropriate. An SQL query is performed for each exercise in the template, and this query returns all exercises that fit the given muscle group, type of movement (compound or isolation), weight, limitations, equipmant, and difficulty. A random exercise from that list is then picked. The more exercises needed in a routine, the lower the  required weight drops. I found this method to be most effective as allows for more variety the deeper you go in a workout.  

Optimizations
(optional)

You don't have to include this section but interviewers love that you can not only deliver a final product that looks great but also functions efficiently. Did you write something then refactor it later and the result was 5x faster than the original implementation? Did you cache your assets? Things that you write in this section are GREAT to bring up in interviews and you can use this section as reference when studying for technical interviews!

Lessons Learned:
No matter what your experience level, being an engineer means continuously learning. Every time you build something you always have those whoa this is awesome or wow I actually did it! moments. This is where you should share those moments! Recruiters and interviewers love to see that you're self-aware and passionate about growing.

Examples:
Take a look at these couple examples that I have in my own portfolio:

Palettable: https://github.com/alecortega/palettable

Twitter Battle: https://github.com/alecortega/twitter-battle

Patch Panel: https://github.com/alecortega/patch-panel

