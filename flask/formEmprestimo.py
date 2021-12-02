from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class EmprestimoForm(FlaskForm):
    ficha = SelectField('Ficha', coerce=int)
    livro = SelectField('Livro', coerce=int)
    enviar = SubmitField('EMPRESTAR')
