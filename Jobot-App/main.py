from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from constants import *

app = Flask(__name__, template_folder='webpages')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config.from_object('constants')
app.secret_key = "Jobot"

import views
from models import db
