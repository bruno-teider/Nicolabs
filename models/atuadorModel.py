from database.config import db

class Atuador(db.Model):
  __tablename__ = 'atuadores'
  id = db.Column('id', db.Integer, primary_key=True)
  apelido = db.Column(db.String(50))
  ativo = db.Column(db.Boolean)
  tipo = db.Column(db.String(50))