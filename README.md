# cs50_final

# Todo Program

Hello, my name is Sam I go by SamIG and this is my Todo Program
### Video Demo:  https://www.youtube.com/watch?v=Gzl6M4Tha_c
### Description:
so for using this you need to do a couple of installation things which I explained [here](#instalation)

**Please note that this is just a prototype (right now program works with localstorage!)**

Ok now that you can use this code let me tell you what it is:

### TM
ok this is the part that I started with(**right now there is a todo list ready to use**), I will say shortly it will be a complete TaskManager(also this one is going to be on the mobile application for the notifications and etc)
it's going to be like some sort of a calendar but not a calendar just a TaskManager!! honestly, it is just a todo list with more abilities((:
now how it works:
first the flask is the base for the website, as you can check in the **app.py**
we import a bunch of stuff let's see what are they!
from flask import Flask, render_template, redirect, url_for, flash -> using all of this for the website to run!
from flask_sqlalchemy import SQLAlchemy -> using this one to connect to our database
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user -> used for login and logout
from flask_wtf import FlaskForm -> using it to create forms(register and login)
from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, SubmitField -> using these parts for details in our form
from wtforms.validators import InputRequired, Length, ValidationError -> check the input in the form sent by the user
from flask_bcrypt import Bcrypt -> using this system to hash the password(we don't want to save the exact password do we?)

app = Flask(__name__, static_url_path='', static_folder='static') -> now we just make our app and also set our static path so it can find the css and js files!
database config is very simple just set the DB for the app and tell it what's the name of our database file!
don't forget we need a secret key for our website in production we don't share secret key but here i allow it who cares!
login config is just basic configuration that you can find in flask_login documentation
now the fun part, we create our User with a class give it username and password and ofcourse and user_id
register and login forms are the same here there is just a username and password field and then submit
our first route is the main one "/" that takes us to the home page of the website
next we have dashboard that user after login can access to it and find the togo program in there
in login we just simply send the templates to the user and after he POST the info to us we just check for existing username and for the currect password
logout the easy one just say logout_user() and we're done!
rigister is just like login we check that there no username exist! and then hash the password and save it to our database
then we get to the todo part where we need to be logedin fot getting access to it:

now how does this todo work?
if you check the todo.js in the static folder you see at first we connect to the localstorage, then we check for existing todos in there and if there is none we create some default todos for fun!
now there is our main function that creates todos let's see what it does:
first we take the todo list from the page and cleare everything inside it!!!
now for each todo inside the localstorage we just simply add them to the innerHTML of todo_list with some button for delete and edit(the edit part doesn't work but you get the idea!)
now how does this delete button works? well we first get the button that we just created and add a EventListener to it so when user click on it it just remove that selected todo from the localstorage
here we just call this function and we're done but we have **add** and **search** part too!
first we get the add and search and all we do is just add a Eventlistener to it so we it's clicked it shows a form
here for add everything in that form will be submit and add to our localstorage as a new todo then we call the createtodo function to show all the todos again
there is a feacher here if user don't submit any date we just put the current date in that todo ohterwise we add the date user gave us
for seach things are a little different first we just lowercase the input then we get all the todos from localstorage now for each todo we lowecase it and check if it's eaual to the input if it is it will be shown other wise there will be no todo to show
simple right?
## instalation:

---
1. first you need to install [python3](https://www.python.org/) and [sqlite](https://sqlite.org/index.html)
2. now open your terminal/cmd(in windows) and clone this code(or just download the zip file and unzip it somewhere)
3. go to the project folder and type these command:
    `python3 -m venv venv`
    `source venv/bin/activate` OR `venv\Script\activate`(i think this works on windows IDK)
    `pip install -r requirements.txt`
    so basically we just created a environment for this project and installed all the dependencies inside that environment
4. now you have to create the table so:
    `python`
    `from app import db`
    `db.create_all()`
6. finally start the localserver and have fun using it for whatever the reason is
    `python3 app.py`
---
### Tips
- in windows after installing python3 in your cmd you just need to type **python**, so replace all python3 with **python**
