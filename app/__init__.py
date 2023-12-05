from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_oauthlib.client import OAuth
from googleapiclient.discovery import build
from google.oauth2 import service_account

myapp_obj = Flask(__name__)
login = LoginManager(myapp_obj)
login.login_view = 'login'

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_mapping(
    SECRET_KEY = 'my-secret-key', #used for login
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(myapp_obj)
with myapp_obj.app_context():
    from app.models import User, Note
    db.create_all()
    
    
def create_drive_service():
    CLIENT_SECRET_FILE = 'app/credentials.json'
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    credentials = service_account.Credentials.from_service_account_file(
        CLIENT_SECRET_FILE, scopes=SCOPES
    )
    return build('drive', 'v3', credentials=credentials)

drive_service = create_drive_service()

from app import routes