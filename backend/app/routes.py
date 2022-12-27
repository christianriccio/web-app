from flask import render_template, url_for, flash, redirect
from app import app
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Christian Riccio',
        'title': 'Blog post 1',
        'content': 'frist post content',
        'date_posted': 'April 20, 2018'
    },
    {
 'author': 'Christian christian',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account creted for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Log In con successo', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log In failed, please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)