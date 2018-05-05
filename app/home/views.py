from flask import render_template

from app.home import home


@home.route('/')
def index():
    return render_template('home/index.html', title='Welcome')
