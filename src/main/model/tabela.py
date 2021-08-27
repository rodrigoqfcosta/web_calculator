from app import db

class Historico(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_oper=db.Column(db.String(50))
    tipo_oper=db.Column(db.String(50))
    operacao=db.Column(db.String(50))
    argumentos=db.Column(db.String(50))
