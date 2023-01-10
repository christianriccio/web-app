#import os
from flask import Flask
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
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
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
#app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
#app.config['MAIL_PORT'] = 465 #587
#app.config['MAIL_USE_TLS'] = False
#app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
#app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '452f06fcf4a540'
app.config['MAIL_PASSWORD'] = '06d30a4c22548a'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
migrate = Migrate(app, db)


from app.users.routes import users
from app.main.routes import main
from app.posts.routes import posts
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

