from flask import Flask
from flask import session
from waitress import serve
from flask import render_template
from flask import request, url_for, redirect, flash, make_response
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from database import db
from flask_session import Session
import logging
import os
import datetime
import hashlib

from formUsuario import UsuarioForm
from formLogin import LoginForm
from usuario import Usuario


app = Flask(__name__)
bootstrap = Bootstrap(app)
CSRFProtect(app)
CSV_DIR = '/flask/'

logging.basicConfig(filename='/flask/app.log', filemode='w', format='%(asctime)s %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_SSL_STRICT'] = False
Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + CSV_DIR + 'bd.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def inicializar_bd():
    db.create_all()

@app.route('/')
def root():
    return (render_template('index.html'))
        
@app.route('/livros/cadastrar',methods=['POST','GET'])
def cadastrar_livro():
    return(u"Não implementado")

@app.route('/livros/listar')
def listar_livros():
    return(u"Não implementado")

@app.route('/usuario/cadastrar',methods=['POST','GET'])
def cadastrar_usuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        nome = request.form['nome']
        username = request.form['username']
        email = request.form['email']
        telefone = request.form['telefone']
        senha = request.form['senha']
        senhahash = hashlib.sha1(senha.encode('utf8')).hexdigest()
        admin = False
        try:
            if request.form['admin'] == 'y':
                admin = True
        except:
            admin = False
        novoUsuario = Usuario(nome=nome,username=username,email=email,telefone=telefone,senha=senhahash,admin=admin)
        db.session.add(novoUsuario)
        db.session.commit()
        flash(u'Usuário cadastrado com sucesso!')
        return(redirect(url_for('root')))
    return (render_template('form.html', form=form, action=url_for('cadastrar_usuario')))

@app.route('/usuario/listar')
def listar_usuarios():
    usuarios = Usuario.query.order_by(Usuario.nome).all()
    return(render_template('usuarios.html', usuarios=usuarios))

@app.route('/livros/emprestar',methods=['POST','GET'])
def emprestar_chave():
    return(u"Não implementado")

@app.route('/livros/listar_emprestimos')
def listar_emprestimos():
    return(u"Não implementado")

@app.route('/usuario/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = request.form['usuario']
        senha = request.form['senha']
        senhahash = hashlib.sha1(senha.encode('utf8')).hexdigest()
        linha = Usuario.query.filter(Usuario.username==usuario,Usuario.senha==senhahash).all()
        if (len(linha) > 0):
            session['autenticado'] = True
            session['usuario'] = linha[0].id
            session['username'] = linha[0].username
            session['admin'] = linha[0].admin
            flash(u'Usuário autenticado com sucesso!')
            return(redirect(url_for('root')))
        else:
            flash(u'Usuário ou senha não conferem!')
            return(redirect(url_for('login')))
    return (render_template('form.html', form=form, action=url_for('login')))

@app.route('/usuario/logout',methods=['POST','GET'])
def logout():
    session.clear()
    return(redirect(url_for('login')))

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, url_prefix='/app')
