class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@postgresqldb:5432/flasktutorial'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:1486/flasktutorial'