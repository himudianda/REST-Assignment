from flask import Flask

from server.register import blueprints, extensions, error_templates


def create_app(application_name=__name__, settings_override=None):
    """
    Create an application using the Flask app factory pattern:
    http://flask.pocoo.org/docs/0.10/patterns/appfactories

    :return: Flask app
    """
    app = Flask(application_name)
    configure_settings(app, settings_override)

    # Register
    blueprints(app)
    extensions(app)
    error_templates(app)

    return app


def configure_settings(app, settings_override=None):
    """
    Modify the settings of the application (mutates the app passed in).

    :param app: Flask application instance
    :return: Add configuration settings
    """
    app.config.from_object('config.settings')
    if settings_override:
        app.config.update(settings_override)
    return app.config
