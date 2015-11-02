from flask import render_template

from server.extensions import db
from server.blueprints.comment import comment_api
from server.blueprints.page import page
from server.blueprints.comment import comment

FLASK_BLUEPRINTS = [page, comment]
CUSTOM_ERROR_PAGES = [404, 500, 502]


def blueprints(app):
    """
    Register 0 or more blueprints (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    for blueprint in FLASK_BLUEPRINTS:
        app.register_blueprint(blueprint)

    return None


def extensions(app):
    db.init_app(app)
    comment_api.init_app(app)


def error_templates(app):
    """
    Register 0 or more error handlers (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """

    def render_status(status):
        """
         Render a custom template for a specific status.
           Source: http://stackoverflow.com/a/30108946

         :param status: Status as a written name
         :type status: str
         :return: None
         """
        status_code = getattr(status, 'code', 500)
        return render_template('{0}.html'.format(status_code)), status_code

    for error in CUSTOM_ERROR_PAGES:
        # app.errorhandler is a decorator taking error as an argument
        # render_status is the function it decorates
        app.errorhandler(error)(render_status)
    return None
