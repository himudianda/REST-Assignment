from flask_sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth


db = SQLAlchemy()
auth = HTTPBasicAuth()
