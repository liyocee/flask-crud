from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import app_config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)

    # db migration
    migrate = Migrate(app=app, db=db)

    # load all models
    from app import models

    @app.route("/")
    def index():
        return "hello world"

    return app
