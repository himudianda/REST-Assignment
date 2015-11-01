from flask import Flask

from server.register import blueprints

def create_app():
    app = Flask(__name__)

    # Register
    blueprints(app)

    return app
