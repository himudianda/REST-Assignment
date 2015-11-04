import random

import click
from faker import Faker

from server.app import create_app
from server.extensions import db
from server.blueprints.user.models import User
from server.blueprints.comment.models import Comment

fake = Faker()
app = create_app()
db.app = app


def _log_status(count, model_label):
    """
    Log the output of how many records were created.

    :param count: Amount created
    :type count: int
    :param model_label: Name of the model
    :type model_label: str
    :return: None
    """
    click.echo('Created {0} {1}'.format(count, model_label))

    return None


def _bulk_insert(model, data, label):
    """
    Bulk insert data to a specific model and log it.

    :param model: Model being affected
    :type model: SQLAlchemy
    :param data: Data to be saved
    :type data: list
    :param label: Label for the output
    :type label: str
    :return: None
    """
    with app.app_context():
        model.query.delete()
        db.session.commit()
        db.engine.execute(model.__table__.insert(), data)

        _log_status(model.query.count(), label)

    return None


@click.group()
def cli():
    """ Populate your db with generated data. """
    pass



@click.command()
def users():
    """
    Create random users.
    """
    random_usernames = []
    data = []

    # Ensure we get about 50 unique random usernames.
    for i in range(0, 50):
        random_usernames.append(fake.user_name())

    random_usernames = list(set(random_usernames))

    while True:
        if len(random_usernames) == 0:
            break

        username = random_usernames.pop()

        params = {
            'username': username,
            'password': User.encrypt_password('password')
        }

        data.append(params)

    return _bulk_insert(User, data, 'users')



@click.command()
def comments():
    """
    Create random comments.
    """
    data = []
    users = db.session.query(User).all()

    for user in users:
        for i in range(0, random.randint(1, 12)):

            params = {
                'topic': random.choice(Comment.TOPICS.keys()),
                'text': fake.text(max_nb_chars=255),
                'user_id': user.id
            }

            data.append(params)

    return _bulk_insert(Comment, data, 'comments')


@click.command()
@click.pass_context
def all(ctx):
    """
    Populate everything at once.

    :param ctx:
    :return: None
    """
    ctx.invoke(users)
    ctx.invoke(comments)

    return None


cli.add_command(users)
cli.add_command(comments)
cli.add_command(all)
