from flask import render_template
from app import myapp_obj
from datetime import date

@myapp_obj.route("/")
def main_page():
    return ("Welcome to main page")

@myapp_obj.route("/hello")
def hello():
    return ("Hello CMPE 131")

@myapp_obj.route("/printScreen/<string:name>")
def page_name(name):
    return (name)

@myapp_obj.route("/Sam")
def greet():
    now = date.today()
    names = ['bob', 'billy']
    return render_template('welcome.html', name='Sam', now=now, names=names)