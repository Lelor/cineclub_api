from os import urandom

from flask import Flask
from flask_jwt_extended import JWTManager

from app.models import db


def create_app(file_name='config/development.py'):
    app = Flask(__name__)
    db.init_app(app)
    JWTManager(app)
    app.secret_key = urandom(24)
    app.config.from_pyfile(file_name)

    # registering blueprints
    from app.blueprints.registration import bp as registration_bp
    app.register_blueprint(registration_bp)

    return app