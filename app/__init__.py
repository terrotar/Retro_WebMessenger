from flask import Flask
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'PedroChallenge'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user_db/sqlite_user.db"

socketio = SocketIO(app, cors_allowed_origins="*")

login_manager = LoginManager(app)

db = SQLAlchemy(app)
