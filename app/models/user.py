from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, server_default=text("nextval('user_id_seq'::regclass)"))
    username = Column(String(20))
    password = Column(String(20))

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

#for migration
# from app.app import db, app

# class User(db.Model):
#     __table__name = 'users'

#     id = db.Column(db.Integer, primary_key=True) #not need autoincrement=True
#     username = db.Column(db.String(20))
#     password = db.Column(db.String(20))

#     def __init__ (self, username, password):
#         self.username = username
#         self.password = password

#     @property
#     def serialize(self):
#        """Return object data in easily serializable format"""
#        return {
#            'id': self.id,
#            'username': self.username,
#            'password': self.password,
#        }

#for autogenerate exist database
# coding: utf-8