# -*- coding: utf-8 -*-

"""Main module."""

from flask import Flask
from flask_migrate import Migrate
from .database import db
from .config import DevConfig


def create_app(config_object=DevConfig):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    # Override from the config.py on the instance folder
    app.config.from_pyfile('config.py', silent=True)

    # Init the database
    db.init_app(app)

    # Init the migration modules
    # TODO: Makes sure this works
    migrate = Migrate(app, db)

    return app
