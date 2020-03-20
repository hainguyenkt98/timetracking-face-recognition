#database connect
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#models
from .user import User