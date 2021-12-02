from sqlalchemy.orm import backref
from database import db
from sqlalchemy.sql import func

class Emprestimo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer,db.ForeignKey('usuario.id'))
    id_livro = db.Column(db.Integer,db.ForeignKey('livro.id'))
    id_ficha = db.Column(db.Integer,db.ForeignKey('ficha.id'))
    data_emprestimo = db.Column(db.DateTime, unique=False, nullable=False, default=func.now())
    data_devolucao = db.Column(db.DateTime, unique=False, nullable=True)
