import pytest

from config import settings
from server.app import create_app
from server.extensions import db as _db
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
        'WTF_CSRF_ENABLED': False,
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

    params = {
        'topic': 'health',
        'text': 'Some health test comment'
    }

    seed_comment = Comment(**params)
    _db.session.add(seed_comment)
    _db.session.commit()

    return _db


# Model fixtures --------------------------------------------------------------
@pytest.fixture(scope='function')
def comments(db):
    """
    Create comment fixtures. They reset per test.

    :param db: Pytest fixture
    :return: SQLAlchemy database session
    """
    db.session.query(Comment).delete()

    comments = [
        {
            'topic': 'health',
            'text': "Red wine may be good for health."
        },
        {
            'topic': 'politics',
            'text': "Could Jeb Bush lose the republican primary ?"
        },
        {
            'topic': 'tech',
            'text': 'Exablox - the next big storage startup'
        }
    ]

    for comment in comments:
        db.session.add(Comment(**comment))

    db.session.commit()

    return db
