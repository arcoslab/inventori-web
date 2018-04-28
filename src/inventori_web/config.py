import os


class Config(object):
    """Base Configuration"""
    SECRET_KEY = os.environ.get('{{cookiecutter.app_name | upper}}_SECRET', 'secret-key')  # TODO: Place this on instance folder config.py # noqa
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(object):
    """Development environment configuration"""
    ENV = "dev"
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    # TODO: Put this on the instance folder
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    DEBUG_TB_ENABLED = True
