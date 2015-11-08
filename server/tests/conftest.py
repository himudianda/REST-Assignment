import pytest
import random

from config import settings
from server.app import create_app
from server.extensions import db as _db
from server.blueprints.user.models import User
from server.blueprints.comment.models import Comment

# App and database fixtures ---------------------------------------------------
@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """
    db_uri = '{0}_test'.format(settings.SQLALCHEMY_DATABASE_URI)
    params = {
        'DEBUG': False,
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': db_uri
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()

@pytest.fixture(scope='session')
def db(app):
    """
    Setup our database, this only gets executed once per session.

    :param app: Pytest fixture
    :return: SQLAlchemy database session
    """
    _db.drop_all()
    _db.create_all()

    return _db


# Model fixtures --------------------------------------------------------------
@pytest.fixture(scope='function')
def test_data(db):
    db.session.query(User).delete()

    users = [
        {
            'username': 'admin',
            'password': 'password'
        },
        {
            'username': 'user1',
            'password': 'password'
        }
    ]

    for user in users:
        db.session.add(User(**user))

    db.session.commit()

    _users = User.query.all()
    for _u in _users:
        params = {
            'user_id': _u.id,
            'topic': random.choice(Comment.TOPICS.keys()),
            'text': "A fake comment."
        }

        comment = Comment(**params)
        db.session.add(comment)

    db.session.commit()

    return db
