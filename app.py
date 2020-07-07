from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LogInForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "1f1b7ab499afc8179f8d9a908f5ccc82"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)
from models import User, Post

posts = [
    {
        'author': 'Anne Hathaway',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Cooper Smith',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
def home():
    return render_template("home.html", posts = posts, title = "yay a home title")

@app.route("/about")
def about():
    return render_template("about.html", title = "the brand new title :D")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}')
        return redirect(url_for('home'))
    return render_template("register.html", title = "Sign Up", form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in", "Success!")
            return redirect(url_for('home'))
    return render_template("login.html", title = "Log In", form = form)


if __name__ == "__main__":
    app.run(debug = True)
