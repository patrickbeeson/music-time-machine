import logging
from logging.handlers import RotatingFileHandler, SMTPHandler
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

from . import views

ADMINS = app.config['ADMINS']
MAIL_SERVER = app.config['MAIL_SERVER']
MAIL_USERNAME = app.config['MAIL_USERNAME']
MAIL_PASSWORD = app.config['MAIL_PASSWORD']
SERVER_EMAIL_ADDRESS = app.config['SERVER_EMAIL_ADDRESS']
SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']
SECRET_KEY = app.config['SECRET_KEY']

db = SQLAlchemy(app)

credentials = (
    MAIL_USERNAME,
    MAIL_PASSWORD
)

if not app.debug:
    file_handler = RotatingFileHandler(
        'errors.log',
        maxBytes=10000,
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    mail_handler = SMTPHandler(
        MAIL_SERVER,
        SERVER_EMAIL_ADDRESS,
        ADMINS,
        'An error has occured',
        credentials=credentials
    )
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

if __name__ == '__main__':
    app.run()
