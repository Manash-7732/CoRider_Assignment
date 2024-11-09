# Flask MongoDB CRUD API

This application provides a REST API for performing CRUD (Create, Read, Update, Delete) operations on a **User** resource. The application is built using **Flask** and **MongoDB**, with a focus on scalability, clean code structure, and best practices in system design.

## Features

- **User Resource**:
  - **id**: A unique identifier for the user.
  - **name**: The name of the user.
  - **email**: The email address of the user.
  - **password**: The password of the user.

- **REST API Endpoints**:
  - **GET /users**: Returns a list of all users.
  - **GET /users/<id>**: Returns the user with the specified ID.
  - **POST /add**: Creates a new user with the specified data.
  - **PUT /update/<id>**: Updates the user with the specified ID with the new data.
  - **DELETE /delete/<id>**: Deletes the user with the specified ID.

## System Requirements

Before getting started, make sure you have the following installed:

- Python 3.x
- Docker
- MongoDB (Dockerized or locally running)

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Manash-7732/CoRider_Assignment.git
   cd CoRider_Assignment


## how to setup env
-use the .env.example for refrences

## requirements and library
-<pip install>
-Flask==3.0.3
-flask-pymongo==2.3.0
-werkzeug==3.0.3
-pymongo==4.10.1
-python-dotenv==1.0.1


## How to run Locally
- python3 app.py

## how to build docker file

docker build -it <image name>:<tag-name>
docker run -it -p 5000:5000 <image-name>





