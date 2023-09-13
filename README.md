# Flask API for Managing Persons

This Flask API allows you to manage a collection of persons, with support for basic CRUD (Create, Read, Update, Delete) operations. It utilizes Flask, Flask-RESTful, and Flask-SQLAlchemy for building and interacting with a SQLite database.

## Authors

- [@DonaldEOgbame](https://github.com/DonaldEOgbame)

## Getting Started

### Prerequisites

Before you begin, ensure you have Python and pip installed. You will also need to install the required Python packages listed in the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

## Running the API
To run the API, execute the following command:

```bash
python main.py
```
By default, the API will run in debug mode.

### API Endpoints
#### Retrieve a Person
Retrieve a person by either their ID or name:

* URL: /api/<person_id_or_name>
* Method: GET
* Example: /api/1 or /api/JohnDoe

#### Update a Person
Update a person's name:

* URL: /api/<person_id_or_name>
* Method: PATCH
* Example: /api/1
* Data: { "name": "NewName" }

#### Delete a Person
Delete a person by either their ID or name:

* URL: /api/<person_id_or_name>
* Method: DELETE
* Example: /api/1 or /api/JohnDoe

#### Create a Person with a Specified ID
Create a new person with a specific ID:

* URL: /api/<int:person_id>
* Method: POST
* Example: /api/2
* Data: { "name": "JohnDoe" }

### Database
This API uses SQLite as its database, with a person_database.db file. The database schema includes a person_model table with id and name columns.

### Usage Notes
When updating a person's name, make a PATCH request with the new name data.
When creating a person with a specific ID, make a POST request to the /api/<int:person_id> endpoint.
