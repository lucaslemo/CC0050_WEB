from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Optional

class BuscaFichaForm(FlaskForm):
    campo = StringField('Buscar: ', validators=[DataRequired()])
    enviar = SubmitField('BUSCAR')
