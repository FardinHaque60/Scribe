from flask import render_template, redirect, flash
from flask_login import current_user, login_user, login_required, logout_user
from app import myapp_obj, db
from datetime import date
from .forms import LoginForm, CreateAccount
from .models import User



@myapp_obj.route("/home")
@login_required # users cannot access this function that are not authenticated
def main_page():
    name = "temp" #add some way to call db and get the name here
    return render_template('home.html', name=name)

# login function also serves as the default page (until changed?)
@myapp_obj.route("/")
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    # checks if user is logged in
    if current_user.is_authenticated:   
        return redirect('/home')
    form = LoginForm()
    
    if form.validate_on_submit():
        # queries database to find the user
        user = User.query.filter_by(username=form.username.data).first()
        # checks password hash with attached to the user the user
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect("/login")
        # Flask-Login function registers the user as logged in
        login_user(user, remember=form.remember_me.data)
        return redirect('/home')
    return render_template('login.html', form=form)

# logout function
@myapp_obj.route("/logout")
def logout():
    # # Flask-Login function registers the user as logged out
    logout_user()
    
    return redirect ("/")
# create account function
@myapp_obj.route("/create_account", methods=['GET', 'POST'])
def create_account():
    # checks if user is logged in
    if current_user.is_authenticated:
        return redirect('/index')
    form = CreateAccount()
    if form.validate_on_submit():
        u = User(username=form.username.data, email=form.email.data)
        u.set_password(form.password.data)  # sets password hash
        db.session.add(u)
        db.session.commit()
        flash('New Account Created')
        return redirect('/login')
    return render_template("create_account.html", form=form)



@myapp_obj.route("/trash_folder")
def trash_folder():
    return render_template("trash_folder.html")
