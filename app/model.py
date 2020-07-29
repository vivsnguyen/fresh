"""Playlist creator project."""

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):

        return f"<User id={self.id}, name={self.name}>"

class Location(db.Model):
    """Location."""

    __tablename__ = "locations"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    loc_type = db.Column(db.String(50), nullable=False)
    is_open = Column(db.Boolean, unique=False, default=True)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)