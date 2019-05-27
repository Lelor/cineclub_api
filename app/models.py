from datetime import datetime, timedelta

import jwt
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()
db_uri = 'sqlite:////pi05/app.db'


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(40), nullable=False)
    email = Column(String(40), nullable=False)
    birthdate = Column(Date, nullable=False)
    created_at = Column(Date, default=datetime.now())
    updated_at = Column(Date, default=datetime.now())

    def hash_password(self):
        """Hashes the entity password."""
        self.password = generate_password_hash(self.password)

    def authenticate(self, password: str):
        """Authenticates the user and generates a token"""
        if check_password_hash(self.password, password):
            return self.generate_token()

    def generate_token(self):
        """
        Generates the JWT token with a 20min expiration and the user id.
        """
        expiration = datetime.utcnow() + timedelta(minutes=20)
        payload = {
            'exp': expiration,
            'user': self.id
        }
        return jwt.encode(payload, current_app.secret_key).decode('utf-8')

class MovieGenre(db.Model):
    id = Column(Integer, primary_key=True)
    text = Column(String(30), nullable=False)


class Movie(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    release_date = Column(Date)
    director = Column(String)
    genre_id = Column(Integer, ForeignKey('movie_genre.id'))
    genre = relationship("MovieGenre")
