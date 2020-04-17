from flask import Flask
from configs.dev import DevelopmentConfig

app = Flask(__name__)

def create_app(config=DevelopmentConfig):

    app.config.from_object(config)

    #blueprint
    from routes.home.home import home
    from routes._face_recognition._face_recognition import _face_recognition

    #apply blueprint
    app.register_blueprint(home, url_prefix='/home')
    app.register_blueprint(_face_recognition, url_prefix='/face-recognition');

    return app