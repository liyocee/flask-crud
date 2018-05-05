# Employee management app using flask

This projects implements all the CRUD functionality for an employee management web app using flask.

It leverages:

- Flask web framework
- SQLAlchemy ORM
- Mysql Database


It also demonstrates how to use a scalable folder structure for flask based apps


# Setup

- Set `env` variable:
    - `export FLASK_APP=run.py`
    - `export ENV=dev`
- Create migration repository: `flask db init`
- Create first migration: `flask db migrate`
- Apply db migration `flask db upgrade`


# Run the app

- `flask run`
