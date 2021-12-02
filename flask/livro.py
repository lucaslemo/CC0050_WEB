from database import db

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), unique=False, nullable=False)
    autor = db.Column(db.String(80), unique=False, nullable=False)
    genero = db.Column(db.String(120), unique=False, nullable=False)
