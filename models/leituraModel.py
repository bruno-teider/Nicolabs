from database.config import db
from datetime import datetime

class Leitura(db.Model):
  __tablename__ = 'leituras'
  id = db.Column('id', db.Integer, primary_key=True)
  sensor = db.Column(db.String(50))
  medicao = db.Column(db.String(50))
  data = db.Column(db.DateTime, default=datetime.now)
  