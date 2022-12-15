from flask import Flask
from dotenv import load_dotenv

load_dotenv('./.flaskenv')

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello world </h1>'

if __name__ == '__main':
    app.run()