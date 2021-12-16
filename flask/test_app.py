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

def login(client, username):
    userTest = dict(usuario=username, senha='123321')
    return client.post('/usuario/login',
                        data=userTest,
                        follow_redirects=True)

def logout(client):
    return client.get('/usuario/logout', follow_redirects=True)

def test_0_index(client):
    rv = client.get('/')
    assert 500 != rv.status_code

def test_1_login(client):
    rv = client.get('/livro/cadastrar', follow_redirects=True)
    assert b'Login de Usu' in rv.data
    assert b'Senha:' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_2_login(client):
    rv = login(client, 'admin')
    assert b'autenticado com sucesso!' in rv.data
