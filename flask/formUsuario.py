from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Optional, AnyOf

class UsuarioForm(FlaskForm):
    nome = StringField('Nome: ', validators=[DataRequired()], render_kw={"placeholder": 'Insira o nome'})
    username = StringField(u'Nome de usuário: ', validators=[DataRequired()], render_kw={"placeholder": u'Insira o nome de usuário'})
    email = EmailField('E-mail: ', validators=[DataRequired()], render_kw={"placeholder": 'Insira o E-mail'})
    telefone = StringField('Telefone: ', validators=[DataRequired()], render_kw={"placeholder": 'Insira o telefone'})
    senha = PasswordField('Senha: ', validators=[DataRequired()], render_kw={"placeholder": 'Insira a senha'})
    admin = BooleanField('Administrador', validators=[Optional()])
    enviar = SubmitField('CADASTRAR')
