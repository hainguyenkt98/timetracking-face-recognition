from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configs.dev import DevelopmentConfig

db = SQLAlchemy()
app = Flask(__name__)

def create_app(config=DevelopmentConfig):

    app.config.from_object(config)
    #db.init_app(app)

    #blueprint
    from routes.home.home import home
    #from routes.users.users import users

    #apply blueprint
    app.register_blueprint(home, url_prefix='/home')
    #app.register_blueprint(users, url_prefix='/users')

    return app