from app import app
import pytest

aplicacao = app.test_client()

@pytest.fixture
def client():
    return (aplicacao)

@pytest.fixture
def preparacao():
    app.config['WTF_CSRF_ENABLED'] = False
    yield
    app.config['WTF_CSRF_ENABLED'] = True

def login(client, username, senha):
    userTest = dict(usuario=username, senha=senha)
    return client.post('/usuario/login',
                        data=userTest,
                        follow_redirects=True)

def logout(client):
    return client.get('/usuario/logout', follow_redirects=True)

def test_0_index(client):
    rv = client.get('/')
    assert 500 != rv.status_code

def test_1_login_redirect(client):
    rv = client.get('/livro/cadastrar', follow_redirects=True)
    assert b'Login de Usu' in rv.data
    assert b'Senha:' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_2_login_errado(client):
    rv = login(client, 'usuarioNaoExistente', '123123')
    assert b'rio ou senha n' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_3_login(client):
    rv = login(client, 'admin', '123321')
    assert b'autenticado com sucesso!' in rv.data

def test_4_usuario_listar(client):
    rv = client.get('/usuario/listar', follow_redirects=True)
    assert b'ID' in rv.data
    assert b'Nome de Usu' in rv.data
    assert b'E-mail' in rv.data
    assert b'Administrador' in rv.data

def test_5_livro_listar(client):
    rv = client.get('/livro/listar', follow_redirects=True)
    assert b'ID' in rv.data
    assert b'tulo' in rv.data
    assert b'Autor' in rv.data
    assert b'Dispon' in rv.data

def test_6_ficha_listar(client):
    rv = client.get('/ficha/listar', follow_redirects=True)
    assert b'ID' in rv.data
    assert b'Nome' in rv.data
    assert b'CPF' in rv.data
    assert b'Livros Lidos' in rv.data

def test_7_emprestimos_listar(client):
    rv = client.get('/emprestimo/listar', follow_redirects=True)
    assert b'ID' in rv.data
    assert b'Respons' in rv.data
    assert b'Dono da Ficha' in rv.data
    assert b'Data do Empr' in rv.data

def test_8_livro_json(client):
    rv = client.get('/livro/listar/json')
    assert 500 != rv.status_code

def test_9_usuario_json(client):
    rv = client.get('/usuario/listar/json')
    assert 500 != rv.status_code

def test_10_emprestimo_json(client):
    rv = client.get('/emprestimo/listar/json')
    assert 500 != rv.status_code

def test_11_ficha_json(client):
    rv = client.get('/ficha/listar/json')
    assert 500 != rv.status_code

"""@pytest.mark.usefixtures('preparacao')
def test_8_livro_cadastrar(client):
    data = dict(titulo='Livro Teste',
                autor='Autor Teste',
                genero='Genero Teste')
    rv = client.post('/livro/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'Livro cadastrado com sucesso!' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_9_ficha_cadastrar(client):
    data = dict(nome='Nome Teste',
                cpf='12123234300',
                email='teste@email.com')
    rv = client.post('/ficha/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'Ficha cadastrada com sucesso!' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_10_ficha_cadastrar_repetido_cpf(client):
    data = dict(nome='Outro Nome Teste',
                cpf='12123234300',
                email='outro_teste@email.com')
    rv = client.post('/ficha/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'ficha cadastrada com esse E-mail ou CPF' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_11_ficha_cadastrar_repetido_email(client):
    data = dict(nome='Outro Nome Teste',
                cpf='00100200341',
                email='teste@email.com')
    rv = client.post('/ficha/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'ficha cadastrada com esse E-mail ou CPF' in rv.data"""

def test_99_logout(client):
    rv = logout(client)
    assert b'encerrada com sucesso!' in rv.data