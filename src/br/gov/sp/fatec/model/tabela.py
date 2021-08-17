from app import db

class Historico(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    calculo=db.Column(db.String(50))
