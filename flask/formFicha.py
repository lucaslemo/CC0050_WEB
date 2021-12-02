from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FichaForm(FlaskForm):
    nome = StringField('Nome do Leitor: ', validators=[DataRequired()])
    cpf = StringField('CPF do Leitor: ', validators=[DataRequired()])
    email = StringField('Email do Leitor: ', validators=[DataRequired()])
    enviar = SubmitField('CADASTRAR')
