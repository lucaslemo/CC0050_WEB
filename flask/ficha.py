from database import db

class Ficha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), unique=False, nullable=False)
    cpf = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    emprestimo = db.relationship('Emprestimo', backref='ficha', lazy=True)
