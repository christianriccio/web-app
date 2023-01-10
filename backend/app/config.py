import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = 'cbf47b2eab3d3ecb0ba15b46a7e91842'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER='smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '452f06fcf4a540'
    MAIL_PASSWORD = '06d30a4c22548a'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False