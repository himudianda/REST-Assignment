from os import path

APP_NAME = 'rest'
APP_ROOT = path.join(path.dirname(path.abspath(__file__)), '..')

# App settings, most settings you see here will change in production.
SECRET_KEY = 'pickabettersecret'
DEBUG = True
TESTING = False

SERVER_NAME = 'localhost:8000'

# Database settings,
# The username and password must match what's in docker-compose.yml for dev.
db_uri = 'postgresql://rest:bestpassword@localhost:5432/{0}'
SQLALCHEMY_DATABASE_URI = db_uri.format(APP_NAME)
SQLALCHEMY_POOL_SIZE = 5
