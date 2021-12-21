from database import db

class Ficha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), unique=False, nullable=False)
    cpf = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    ativo = db.Column(db.Boolean(), default=False)
    qtdLivros = db.Column(db.Integer, unique=False, nullable=False)
    totalLivros = db.Column(db.Integer, unique=False, nullable=False)
    emprestimo = db.relationship('Emprestimo', backref='ficha', lazy=True)

    def asdict(self):
      return {c.name: getattr(self, c.name) for c in self.__table__.columns}
