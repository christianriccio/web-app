from flask import Flask, render_template, url_for
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv('./.flaskenv')

app = Flask(__name__, template_folder='templates')
#app.config['SQLALCHEMY_BATABASE_URI'] = 'mysql://root:''@localhost/flask'

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

if __name__ == '__main__':
    app.run(debug=True)