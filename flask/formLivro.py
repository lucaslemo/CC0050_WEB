from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LivroForm(FlaskForm):
    titulo = StringField('Titulo do Livro: ', validators=[DataRequired()])
    autor = StringField('Autor: ', validators=[DataRequired()])
    genero = StringField(u'Gênero: ', validators=[DataRequired()])
    enviar = SubmitField('CADASTRAR')
