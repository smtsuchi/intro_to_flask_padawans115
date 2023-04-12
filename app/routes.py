from flask import redirect, render_template, request, url_for
from app import app
from .forms import SignUpForm
from .models import Post, User

@app.route('/')
def homePage():
    people = ['Shoha', 'Sarah', 'Aubrey', "Nicole"]

    more = {
        'hello': 'world'
    }

    return render_template('index.html', pop=people, more=more)

@app.route('/signup', methods=["GET", "POST"])
def signupPage():
    form = SignUpForm()
    
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            # add user to database
            # if User exists:
            #     print(error msg)
            # else:
            # user = User(username, email, password)
        
            # user.saveToDB()
            account = {
                'username': username,
                'email': email
            }
        return render_template('signup.html', form = form, account=account)
    return render_template('signup.html', form = form)

@app.route('/login')
def loginPage():
    return {}