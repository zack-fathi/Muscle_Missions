# Muscle Missions

Welcome to Muscle Missions, a multi-container fitness management web app designed to revitalize your workout routine! Whether you're looking for personalized daily workouts, weekly splits, or an interactive chatbot for fitness advice, Muscle Missions delivers a modern, scalable solution.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Deployment](#deployment)
- [Architecture](#architecture)
- [Database Design](#database-design)
- [Chatbot: LiftBot](#chatbot-liftbot)
- [Future Plans](#future-plans)
- [Lessons Learned](#lessons-learned)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Introduction
Muscle Missions offers a customized fitness experience by creating user-specific daily workouts, weekly workout splits, and providing motivational and workout support via an interactive chatbot. Whether you're a beginner or an advanced lifter, this app generates fresh, effective workouts that fit your schedule, goals, and available equipment.

## Features
- **Custom Workouts:** Generate tailored workout plans based on user experience, time constraints, and equipment preferences.
- **Interactive Chatbot (LiftBot):** Chat with LiftBot for personalized exercise guidance and motivational support powered by OpenAI GPT-3.5.
- **User Authentication:** Secure sign-in and authentication with personalized workout histories.
- **Microservices Architecture:** Deploy separate containerized services (auth, workout generation, chatbot) using Docker Compose.
- **Responsive Frontend:** An interactive front end built with React and Bootstrap for a mobile-friendly experience.
- **CI/CD:** Automated builds and deployments via GitHub Actions.

## Tech Stack
- **Frontend:** React, Bootstrap  
- **Backend:** Python (Flask)  
- **Database:** SQLite  
- **Chatbot:** OpenAI GPT-3.5  
- **Containerization & Deployment:** Docker, Docker Compose, Nginx  
- **CI/CD:** GitHub Actions  
- **Cloud Hosting:** DigitalOcean  
- **Additional Skills:** Microservices Architecture, RESTful API design, Linux

## Deployment
Muscle Missions is automatically deployed via GitHub Actions:
- **CI/CD Pipeline:** On every push to the main branch, GitHub Actions builds Docker images and deploys the app to DigitalOcean.
- **Docker Compose:** Orchestrates multiple services (auth_server, workouts_server, liftbot_server, frontend, and proxy) in a containerized environment.
- **Production URL:** [https://musclemissions.fit](https://musclemissions.fit)  

## Architecture
- **Auth Server:** Manages user sign-up, login, and session handling; stores user data securely in SQLite.
- **Workouts Server:** Generates customized daily workouts and weekly splits via RESTful APIs.
- **LiftBot Server:** Provides real-time, personalized fitness guidance using OpenAI GPT-3.5.
- **Frontend:** A React application styled with Bootstrap that communicates with backend services via RESTful APIs.
- **Proxy (Reverse Proxy):** An optional Nginx Proxy Manager handles SSL termination and routes incoming traffic to the appropriate service.

## Database Design
Muscle Missions uses SQLite for efficient data management. The database includes:
- **Users:** Stores account information and hashed passwords.
- **Exercises:** Contains a comprehensive directory of over 270 exercises with detailed attributes.
- **Workouts & Splits:** Manages user-specific workout plans and weekly schedules.

## Chatbot: LiftBot
LiftBot is powered by OpenAI GPT-3.5 and offers real-time, personalized fitness advice, exercise tips, and motivational support through an interactive chat interface integrated into the frontend.

## Future Plans
- **Video Integration:** Embed exercise demo videos to enhance workout instructions.
- **Expanded Exercise Library:** Continuously update and refine the exercise database and workout algorithms.
- **Progress Tracking:** Implement analytics and performance tracking with visual dashboards.
- **Community Features:** Develop social features like member forums and workout challenges.

## Lessons Learned
Creating Muscle Missions was a journey of passion, combining my love for fitness with technology. The project honed my skills in containerization & microservices using Docker Compose, CI/CD implementation via GitHub Actions, robust user authentication, and efficient RESTful API design.

## Contact
For more information or collaboration opportunities, please email: [zackeryfathi@gmail.com](mailto:zackeryfathi@gmail.com)

## Acknowledgments
- **StrengthLog:** Provided reference workouts for the exercise database.
- **Unsplash & OpenAI DALL-E:** Sources for images and AI-generated artwork.
- **OpenAI GPT-3.5:** Powers the interactive LiftBot chat functionality.
