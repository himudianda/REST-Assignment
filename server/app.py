from flask import Flask

from server.register import blueprints


def create_app():
    """
    Create an application using the Flask app factory pattern:
    http://flask.pocoo.org/docs/0.10/patterns/appfactories

    :param application_name: Name of the application
    :param settings_override: Override settings
    :type settings_override: dict
    :return: Flask app
    """
    app = Flask(__name__)

    # Register
    blueprints(app)

    return app
