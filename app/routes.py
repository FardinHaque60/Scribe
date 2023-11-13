from flask import render_template
from app import myapp_obj
from datetime import date
from .forms import LoginForm, CreateAccount

@myapp_obj.route("/")
def main_page():
    return render_template('home.html')

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    ''' this is the code for validation below, and flashing to db
    if form.validate_on_submit():
        flash(f'Here are the input {form.username.data} and {form.password.data}')
        return redirect('/')
    '''
    return render_template('login.html', form=form)

@myapp_obj.route("/create_account")
def create_account():
    form = CreateAccount()
    return render_template("/create_account.html", form=form)

#create routes like
#@myapp_obj.route("/<note_name>") so that you can use that input name within the page itself, but doubles as the address