from .config import Config

class ProductionConfig(Config):
    PRODUCTION = True
    DEBUG = False