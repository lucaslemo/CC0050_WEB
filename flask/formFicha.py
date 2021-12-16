from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FichaForm(FlaskForm):
    nome = StringField('Nome do Leitor: ', validators=[DataRequired()], render_kw={"placeholder": 'Insira o nome'})
    cpf = StringField('CPF do Leitor: ', validators=[DataRequired()], render_kw={"placeholder": 'Insira o CPF'})
    email = StringField('Email do Leitor: ', validators=[DataRequired()], render_kw={"placeholder": 'Insira o E-mail'})
    enviar = SubmitField('CADASTRAR')
