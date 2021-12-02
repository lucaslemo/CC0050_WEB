from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Optional, AnyOf

class UsuarioForm(FlaskForm):
    nome = StringField('Nome: ', validators=[DataRequired()])
    username = StringField(u'Nome de usuário: ', validators=[DataRequired()])
    email = EmailField('E-mail: ', validators=[DataRequired()])
    telefone = StringField('Telefone: ', validators=[DataRequired()])
    senha = PasswordField('Senha: ', validators=[DataRequired()])
    admin = BooleanField('Administrador', validators=[Optional()])
    enviar = SubmitField('CADASTRAR')
