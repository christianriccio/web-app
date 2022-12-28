from flask import Flask
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate

load_dotenv('./.flaskenv')

app = Flask(__name__, template_folder='templates')
#app.config['SECRET_KEY'] = 'cbf47b2eab3d3ecb0ba15b46a7e91842'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

from app import routes