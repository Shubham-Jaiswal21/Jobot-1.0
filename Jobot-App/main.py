from flask import Flask
from constants import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__, template_folder='webpages')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.secret_key = "Jobot"

import views
from models import db