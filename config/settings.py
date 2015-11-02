from os import path
from datetime import timedelta

APP_NAME = 'rest'

# App settings, most settings you see here will change in production.
SECRET_KEY = 'pickabettersecret'
DEBUG = True
TESTING = False

# Database settings,
# The username and password must match what's in docker-compose.yml for dev.
db_uri = 'postgresql://rest:bestpassword@localhost:5432/{0}'
SQLALCHEMY_DATABASE_URI = db_uri.format(APP_NAME)
SQLALCHEMY_POOL_SIZE = 5

