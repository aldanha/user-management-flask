# User Management API

The User Management API is an HTTP server built using Python Flask. It provides endpoints for user authentication, user registration, and user management. The API uses SQLite as the database to store user information securely.

## Features

- User Authentication (Login) with JWT Token
- User Registration
- Show Users
- Adding New Users
- Removing Users

## Requirements

- Flask==2.3.2
- Flask-RESTful==0.3.10
- Flask-SQLAlchemy==3.0.5
- PyJWT==2.7.0
- SQLAlchemy==2.0.18

## API Endpoints
- POST /login: User authentication. Returns a JWT token upon successful login.
- POST /register: User registration. Register a new user.
- GET /users: Retrieve a list of all users (Requires JWT token for authorization).
- POST /users/add: Add a new user to the database (Requires JWT token for authorization).
- DELETE /users/remove: Remove a user from the database (Requires JWT token for authorization).

## Authorization
Using JWT token Authorization with 'Bearer' scheme for /users, /users/add, and /users/remove endpoints.

## Project Setup 
- Initialize virtualenv 
    - virtualenv venv
    - source venv/bin/activate 
- Install Dependencies
    - pip install -r requirements.txt
- Run the app
    - python3 app.py
