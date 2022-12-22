from flask import Flask, render_template, url_for, flash, redirect
from dotenv import load_dotenv
from forms import RegistrationForm, LoginForm

load_dotenv('./.flaskenv')

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'cbf47b2eab3d3ecb0ba15b46a7e91842'

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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
    app.run(debug=True)