from sqlalchemy.orm import backref
from database import db

class Emprestimo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer,db.ForeignKey('usuario.id'))
    id_livro = db.Column(db.Integer,db.ForeignKey('livro.id'))
    id_ficha = db.Column(db.Integer,db.ForeignKey('ficha.id'))
    data_emprestimo = db.Column(db.DateTime, unique=False, nullable=False)
    data_devolucao = db.Column(db.DateTime, unique=False, nullable=True)

    def asdict(self):
      resultado = dict()
      for c in self.__table__.columns:
        if getattr(self, c.name) is not None and (c.name == "data_emprestimo" or c.name == "data_devolucao"):
          resultado[c.name]= getattr(self, c.name).strftime('%d/%m/%Y %H:%M')
        else:
          resultado[c.name]= getattr(self, c.name)
      return resultado
