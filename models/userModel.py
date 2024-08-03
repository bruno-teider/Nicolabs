from database.config import db

class Users(db.Model):
  __tablename__ = 'users'
  id = db.Column('id', db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  email = db.Column(db.String(50))
  senha = db.Column(db.String(50))
  admin = db.Column(db.Boolean)
  operador = db.Column(db.Boolean)