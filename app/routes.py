from flask import redirect, render_template, request, url_for
from app import app
from .forms import LoginForm, PostForm, SignUpForm
from .models import Post, User
from flask_login import  current_user, login_user, logout_user, login_required

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
            user = User(username, email, password)
        
            user.saveToDB()
            account = {
                'username': username,
                'email': email
            }
        return render_template('signup.html', form = form, account=account)
    return render_template('signup.html', form = form)

@app.route('/login', methods=["GET", "POST"])
def loginPage():
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()            
            if user:
                # verify password
                if user.password == password:
                    login_user(user)
                    return redirect(url_for('homePage'))
                else:
                    print('invalid password')
            else:
                print('incorrect username or password')


    return render_template('login.html', form = form)

@app.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('loginPage'))


@app.route('/posts/create', methods=['GET', "POST"])
@login_required
def createPost():
    form = PostForm()
    if request.method == 'POST':
        if form.validate():
            #create post and save to db
            title = form.title.data
            img_url = form.img_url.data
            caption = form.caption.data

            post = Post(title, img_url, caption, current_user.id)

            post.saveToDB()

            return redirect(url_for('showAllPosts'))
    return render_template('createpost.html', form = form)

@app.route('/posts')
def showAllPosts():
    posts = Post.query.all()
    return render_template('posts.html', posts = posts)