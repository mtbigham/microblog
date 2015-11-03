import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
#Tell Flask-Login what view logs users in (for 'next' page functionality)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'temp'))

from app import views, models