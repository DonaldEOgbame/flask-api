
# Project Documentation

## Introduction

Welcome to the official documentation for our Flask-based API project. This project provides a RESTful API for managing person records in a local SQLite database. Whether you're a developer or just curious, this guide will help you understand the project's structure, usage, and how to host it locally.

## Table of Contents

1. **Prerequisites**

2. **Getting Started**
   - Running the Application Locally
3. **API Endpoints**
   - Retrieve a Person
   - Update a Person
   - Delete a Person
   - Create a Person with a Specified ID
4. **Database**
   - `person_model` Table
5. **Error Handling**
6. **Testing**
7. **Deployment (Optional)**
8. **Contributing**
9. **License**
10. **Conclusion**

## Prerequisites

Before diving into the project, please ensure you have the following prerequisites installed on your system:

- **Python:** You'll need Python 3.x to run the application.
- **Flask:** We use Flask, a popular web framework for Python.
- **Flask-RESTful:** This extension simplifies the creation of RESTful APIs in Flask.
- **Flask-SQLAlchemy:** It's used for handling the SQLite database.

You can easily install these packages using `pip`:

```bash
pip install Flask Flask-RESTful Flask-SQLAlchemy
```
## Getting Started
### Running the Application Locally
To run the application on your local machine, follow these steps:

* Open a terminal window and navigate to the project directory:

```bash
cd /path/to/your/project_directory
```
* Execute the main.py script:

```bash
python main.py
```
* The application will run in debug mode and be accessible at http://localhost:5000.

## API Endpoints

### Retrieve a Person

- **Endpoint:** `/api/<person_id_or_name>`
- **HTTP Method:** GET
- **Parameters:**
  - `person_id_or_name` (string): The ID or name of the person to retrieve.
- **Response:**
  - If found, returns a JSON representation of the person.

### Update a Person

- **Endpoint:** `/api/<person_id_or_name>`
- **HTTP Method:** PATCH
- **Parameters:**
  - `person_id_or_name` (string): The ID or name of the person to update.
- **Request Body:**
  - `name` (string): The updated name of the person.
- **Response:**
  - If successful, returns a JSON representation of the updated person.

### Delete a Person

- **Endpoint:** `/api/<person_id_or_name>`
- **HTTP Method:** DELETE
- **Parameters:**
  - `person_id_or_name` (string): The ID or name of the person to delete.
- **Response:**
  - If successful, returns an empty response with a status code of 204 (No Content).

### Create a Person with a Specified ID

- **Endpoint:** `/api/<int:person_id>`
- **HTTP Method:** POST
- **Parameters:**
  - `person_id` (integer): The ID for the new person.
- **Request Body:**
  - `name` (string): The name of the person.
- **Response:**
  - If successful, returns a JSON representation of the created person with a status code of 201 (Created).

## Database

Our project relies on an SQLite database named `person_database.db`. SQLAlchemy is used for database interaction, and it features a single table:

### `person_model` Table

- `id` (Integer, Primary Key): Unique identifier for a person.
- `name` (String, 100 characters, Not Null): The name of the person.

## Error Handling

The application gracefully handles various error scenarios, such as:

- Person not found (HTTP 404)
- Invalid input format or length (HTTP 400)
- Duplicate person ID (HTTP 409)

## Testing

We encourage thorough testing of the API using tools like `curl` or API testing tools like Postman.

## Deployment (Optional)

If you wish to deploy this project to a production server, consider using platforms like Heroku, AWS, or Docker. Ensure that you configure environment variables and security settings appropriately.

## Contributing

We welcome contributions! If you'd like to contribute to the project.


## Conclusion

This comprehensive documentation provides insights into our Flask-based API project, covering essential topics like local hosting, API endpoints, and the database structure. Whether you're running it locally for development, testing, or considering deployment, we aim to ensure you have a smooth experience with our project.

Feel free to reach out if you have any questions, feedback, or suggestions for improvement.





