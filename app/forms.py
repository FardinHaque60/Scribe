from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Optional
from wtforms.widgets import TextArea, TextInput
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
    page_menu = SelectField("Select Page:", choices=[], name='page_menu')
    template_menu = SelectField("Select a Template:", choices = [], name='template_menu')
    title = StringField("Note Title:", validators=[DataRequired()], widget=TextInput())
    body = StringField("Note Body:")

    submit = SubmitField("Enter")

class ViewNote(FlaskForm):
    title = StringField("Title:",  validators=[DataRequired()], widget=TextInput())
    body = StringField("Note Body:",  widget=TextArea())

    submit = SubmitField("Save Changes")

class ViewPage(FlaskForm):
    title = StringField("Title:",  validators=[DataRequired()], widget=TextInput())
    body = StringField("Page Body:", widget=TextArea())

    submit = SubmitField("Save Changes")
    
class CreateTemplate(FlaskForm):
    title = StringField('Template Title:', validators=[DataRequired()], widget=TextInput())
    body = StringField('Template Body:')

    submit = SubmitField("Enter")

class CreatePage(FlaskForm):
    title = StringField("Page Title: ", validators=[DataRequired()], widget=TextInput())
    description = StringField('Page Description: ', validators=[DataRequired()], widget=TextArea())

    submit = SubmitField("Enter")

class NoteManagment(FlaskForm):
    note_id = HiddenField('Note ID')
    recover_note = SubmitField('Recover', validators=[Optional()])
    delete = SubmitField('Delete', validators=[Optional()])

class ShareNote(FlaskForm):
    recipient = StringField('Enter Email:', validators=[DataRequired(), Email()])
    submit = SubmitField('Share', validators=[DataRequired()])

class ViewProfile(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], widget=TextInput())
    email = StringField("Email", validators=[DataRequired(), Email()], widget=TextInput())

    submit = SubmitField("Save Changes")

class ChangePassword(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    new_password2 = PasswordField( 'Repeat New Password', validators=[DataRequired(), EqualTo('new_password')])

    submit = SubmitField("Change Password")