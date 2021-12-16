from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LivroForm(FlaskForm):
    titulo = StringField(u'Título do Livro: ', validators=[DataRequired()], render_kw={"placeholder": u'Insira o título'})
    autor = StringField('Autor do Livro: ', validators=[DataRequired()], render_kw={"placeholder": 'Insira o autor'})
    genero = StringField(u'Gênero do Livro: ', validators=[DataRequired()], render_kw={"placeholder": u'Insira o gênero'})
    enviar = SubmitField('CADASTRAR')
