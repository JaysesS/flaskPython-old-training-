from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import db, User
from .forms import RegisterForm, LoginForm

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    signup = RegisterForm()
    if signup.validate_on_submit():
        user = User.query.filter_by(username = signup.username.data).first()
        email = User.query.filter_by(email = signup.email.data).first()
        if user is None and email is None:
            hash_password = generate_password_hash(signup.password.data, method='sha256')
            new_user = User(username = signup.username.data, 
                            password = hash_password, 
                            email = signup.email.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            flash('User or email already exist!')
    return render_template("signup.html", signup = signup)

@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    signin = LoginForm()
    if signin.validate_on_submit():
        user = User.query.filter_by(username = signin.username.data).first()
        if user and check_password_hash(user.password, signin.password.data):
            login_user(user, remember=signin.remember.data)
            return redirect(url_for('index'))
        else:
            flash('Check input data!')
    return render_template("signin.html", signin = signin)

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('index'))
    return redirect(url_for('index'))