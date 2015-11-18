import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask.ext.openid import OpenID
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)

#Tell Flask-Login what view logs users in (for 'next' page functionality)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'temp'))

###Debug Email / Text Logging###
if not app.debug:
	import logging
	from logging.handlers import SMTPHandler, RotatingFileHandler
	
	#Mail#
	credentials = None
	if MAIL_USERNAME or MAIL_PASSWORD:
		credentials = (MAIL_USERNAME, MAIL_PASSWORD)
	mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@'+MAIL_SERVER, ADMINS, 'Microblog Failure', credentials)
	mail_handler.setLevel(logging.ERROR)
	app.logger.addHandler(mail_handler)
	
	#Text Logging#
	file_handler = RotatingFileHandler('temp/microblog.log', 'a', 1 * 1024 * 1024, 10)
	file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	app.logger.setLevel(logging.INFO)
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	app.logger.info('Microblog Startup')

from app import views, models