from flask import render_template
from app import app

@app.route('/')
def homePage():
    people = ['Shoha', 'Sarah', 'Aubrey', "Nicole"]

    more = {
        'hello': 'world'
    }

    return render_template('index.html', pop=people, more=more)

@app.route('/signup', methods=["GET"])
def signupPage():
    return render_template('signup.html')

@app.route('/login')
def loginPage():
    return {}