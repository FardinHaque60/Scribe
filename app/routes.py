from flask import render_template, redirect, flash
from app import myapp_obj, db
from datetime import date
from .forms import LoginForm, CreateAccount
from .models import User

@myapp_obj.route("/")
@myapp_obj.route("/home")
def main_page():
    name = "temp" #add some way to call db and get the name here
    return render_template('home.html', name=name)

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Here are the input {form.username.data} and {form.password.data}')
        return redirect('/')
    return render_template('login.html', form=form)

@myapp_obj.route("/create_account", methods=['GET', 'POST'])
def create_account():
    form = CreateAccount()
    if form.validate_on_submit():
        flash(f'Here are the input {form.username.data}, {form.password.data}, {form.email.data}')
        u = User(username=form.username.data, password=form.username.data, email=form.email.data)
        db.session.add(u)
        db.session.commit()
        return redirect('/')
    return render_template("create_account.html", form=form)

#create routes like
#@myapp_obj.route("/<note_name>") so that you can use that input name within the page itself, but doubles as the address

@myapp_obj.route("/trash_folder")
def trash_folder():
    return render_template("trash_folder.html")
