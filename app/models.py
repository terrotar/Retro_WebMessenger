from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


# User's model of database
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column(db.String, nullable=False, unique=True)
    _password = db.Column(db.String, nullable=False, unique=False)
    _name = db.Column(db.String, nullable=False, unique=True)
    _email = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, username, password, name, email):
        self._username = username
        # Here the password is hashed when created, so the real password
        # is not stored in DB
        self._password = generate_password_hash(password)
        self._name = name
        self._email = email

    # PROPERTIES of GET and SET private attributes

    # Email
    @hybrid_property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    # Password
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    # Verify the hash password
    def verify_password(self, pwd):
        return check_password_hash(self._password, pwd)

    # Name
    @hybrid_property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # Username
    @hybrid_property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username


# Create all tables
db.create_all()
