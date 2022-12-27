from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from dotenv import load_dotenv
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

load_dotenv('./.flaskenv')

app = Flask(__name__, template_folder='templates')
#app.config['SECRET_KEY'] = 'cbf47b2eab3d3ecb0ba15b46a7e91842'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#from app import routes, models

#Model = db.Model

class User(db.Model):
    '''class to menage the user'''
    id = db.Column(db.Integer, primary_key=True )
    username = db.Column(db.String(20), unique=True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref = 'author', lazy = True)

    def __repr_(self):
        return f"User('{self.username}'), '{self.email}', '{self.image_file}'"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr_(self):
        return f"Post('{self.title}'), '{self.date_posted}')"


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

if __name__ == '__main__':
    app.run(debug=True)