from database.config import db

class Sensor(db.Model):
  __tablename__ = 'sensores'
  id = db.Column('id', db.Integer, primary_key=True)
  apelido = db.Column(db.String(50))
  medicao = db.Column(db.String(5))
  ativo = db.Column(db.Boolean)