from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Optional
from wtforms.widgets import TextArea
from app.models import User, Note


#used for login.html
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me') #do not know how we would implement this, but i guess we can keep this option here for now
    submit = SubmitField('Sign In')

class CreateAccount(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField( 'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Enter a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Enter a different email address.')
        
class SearchForm(FlaskForm):
    searched = StringField("Title", validators=[DataRequired()])
    submit = SubmitField('Enter')
    
class CreateNote(FlaskForm):
    title = StringField("Title", validators=[DataRequired()], widget=TextArea())
    body = StringField("Text Field", validators=[DataRequired()], widget=TextArea())

    submit = SubmitField("Enter")
    
class NoteManagment(FlaskForm):
    note_id = HiddenField('Note ID')
    recover_note = SubmitField('Recover', validators=[Optional()])
    delete = SubmitField('Delete', validators=[Optional()])