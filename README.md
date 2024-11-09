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
   git clone https://github.com/yourusername/flask-mongodb-crud-api.git
   cd flask-mongodb-crud-api
