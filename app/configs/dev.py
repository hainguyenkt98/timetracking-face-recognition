from .config import Config

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True