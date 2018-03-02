from flask import Flask
from config import Config
from flask_login import LoginManager

app2 = Flask(__name__)
app2.config.from_object(Config)

# setup database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app2)
migrate = Migrate(app2, db)

login = LoginManager(app2)

from app import routes