from datetime import timedelta
from os import urandom


SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=20)
JWT_SECRET_KEY = urandom(24)
