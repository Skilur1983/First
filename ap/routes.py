from ap import app
from flask import render_template, flash, redirect, url_for, request
from ap.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from ap.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Metz'},
            'body': 'English, Mother Fucker, do you speak it?' 
        }
    ]
    return render_template("index.html", title = 'Fuck off', posts = posts) 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember = form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('Login.html', title = 'Sign In', form = form)

@app.route('/logout')
def logout():
    login_user()
    return redirect(url_for('index'))