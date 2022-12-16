from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv('./.flaskenv')

app = Flask(__name__, static_folder='/Users/christianriccio/Desktop/workspace/web-app/static', template_folder='/Users/christianriccio/Desktop/workspace/web-app/templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main':
    app.run()