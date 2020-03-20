from . import db

class User(db.Model):
    __table__name = 'users'

    id = db.Column(db.Integer, primary_key=True) #not need autoincrement=True
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __init__ (self, username, password):
        self.username = username
        self.password = password

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id': self.id,
           'username': self.username,
           'password': self.password,
       }