from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configs import *

#blueprint
from routes import users

app = Flask(__name__)
db = SQLAlchemy()

app.config.from_object(DevelopmentConfig)
db.init_app(app)

#import model
from routes.home.home import home
from routes.users.users import users

#apply blueprint
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(home, url_prefix='/home')