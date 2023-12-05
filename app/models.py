from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    notes = db.relationship('Note', backref="author")
    templates = db.relationship('Template', backref = "author")
    pages = db.relationship('Page', backref="author")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<user {self.id}: {self.username}>'
        
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(32), nullable=False)
    title = db.Column(db.String(32), nullable=False)
    body = db.Column(db.String(1000), nullable=False)
    page = db.Column(db.String(32), default=0, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    trashed = db.Column(db.Boolean, default=False)
    trashed_time = db.Column(db.DateTime, index=True, default=datetime.now())
    
    def __repr__(self) -> str:
        return '<Note {}>'.format(self.body)
    
class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    body = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    trashed = db.Column(db.Boolean, default=False)
    trashed_time = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self) -> str:
        return '{}'.format(self.id)
    
class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    trashed = db.Column(db.Boolean, default=False)
    trashed_time = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self) -> str:
        return '{}'.format(self.id)