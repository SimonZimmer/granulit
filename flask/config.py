import os
from werkzeug.security import generate_password_hash

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(object):
    TESTING = True
    WTF_CSRF_ENABLED = False
    VERSION = "test"
    SECRET_KEY = b"12345"
    DEFAULT_USERNAME = "testing"
    DEFAULT_PASSWORD = generate_password_hash("testing")
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
