from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dmitry'}
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
    return render_template('index.html', title = 'Fuck off', user = user, posts = posts) 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me = {}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')
    return render_template('Login.html', title = 'Sign In', form = form)