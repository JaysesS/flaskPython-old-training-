from flask import Flask
from flask_bootstrap import Bootstrap
from .models import db
from . import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'SUPERSECRETKEY'
Bootstrap(app)
app.app_context().push()
db.init_app(app)
db.create_all()
from .views import *