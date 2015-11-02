from flask import Flask

from server.register import blueprints, extensions, error_templates


def create_app():
    """
    Create an application using the Flask app factory pattern:
    http://flask.pocoo.org/docs/0.10/patterns/appfactories

    :return: Flask app
    """
    app = Flask(__name__)
    configure_settings(app)

    # Register
    blueprints(app)
    extensions(app)
    error_templates(app)

    return app


def configure_settings(app):
    """
    Modify the settings of the application (mutates the app passed in).

    :param app: Flask application instance
    :return: Add configuration settings
    """
    app.config.from_object('config.settings')
    return app.config
