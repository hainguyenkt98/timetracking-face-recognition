from flask import Flask
from .configs import *
from .models import db

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    
    #config
    app.config.from_object(DevelopmentConfig)

    #database
    db.init_app(app);

    #register Blueprints
    from .routes import users, home

    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(home, url_prefix='/home')

    return app