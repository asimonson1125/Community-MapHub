from os import environ as env

# automatically updates some dev envs. 
try:
    __import__('envs.py')
except ImportError:
    pass

# Flask config
IP = env.get('IP', '0.0.0.0')
PORT = env.get('PORT', 8080)
SERVER_NAME = env.get('SERVER_NAME', 'localhost:5000')
PREFERRED_URL_SCHEME = env.get('PREFERRED_URL_SCHEME', 'https')

SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = 'False'