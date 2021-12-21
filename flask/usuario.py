from database import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20),unique=False, nullable=False)
    senha = db.Column(db.String(80), unique=False, nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    emprestimo = db.relationship('Emprestimo', backref='usuario', lazy=True)

    def asdict(self):
      return {c.name: getattr(self, c.name) for c in self.__table__.columns}
