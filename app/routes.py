from flask import render_template
from app import app

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