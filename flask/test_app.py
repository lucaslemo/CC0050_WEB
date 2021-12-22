from app import app
import pytest
import json

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

def test_12_busca_livro_nao_existente(client):
    rv = client.get('/livro/livro_nao_existente')
    assert 500 != rv.status_code

def test_13_busca_usuario_nao_existente(client):
    rv = client.get('/usuario/usuario_nao_existente')
    assert 500 != rv.status_code

def test_14_busca_emprestimo_nao_existente(client):
    rv = client.get('/emprestimo/0/0')
    assert 500 != rv.status_code

def test_15_busca_livro_nao_existente(client):
    rv = client.get('/ficha/ficha_nao_existente')
    assert 500 != rv.status_code

@pytest.mark.usefixtures('preparacao')
def test_16_livro_cadastrar(client):
    data = dict(titulo='Livro Teste',
                autor='Autor Teste',
                genero='Genero Teste')
    rv = client.post('/livro/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'Livro cadastrado com sucesso!' in rv.data

def test_17_busca_livro(client):
    rv = client.get('/livro/Livro Teste')
    assert 500 != rv.status_code

def test_18_busca_livro_upper(client):
    rv = client.get('/livro/livro teste')
    assert b'Livro Teste' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_19_ficha_cadastrar(client):
    data = dict(nome='Nome Teste',
                cpf='12123234300',
                email='teste@email.com')
    rv = client.post('/ficha/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'Ficha cadastrada com sucesso!' in rv.data

def test_20_busca_ficha(client):
    rv = client.get('/ficha/12123234300')
    assert 500 != rv.status_code

def test_21_busca_ficha_upper(client):
    rv = client.get('/ficha/12123234300')
    assert b'Nome Teste' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_22_ficha_cadastrar_repetido_cpf(client):
    data = dict(nome='Outro Nome Teste',
                cpf='12123234300',
                email='outro_teste@email.com')
    rv = client.post('/ficha/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'ficha cadastrada com esse E-mail ou CPF' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_23_ficha_cadastrar_repetido_email(client):
    data = dict(nome='Outro Nome Teste',
                cpf='00100200341',
                email='teste@email.com')
    rv = client.post('/ficha/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'ficha cadastrada com esse E-mail ou CPF' in rv.data

def test_30_remover_livro(client):
    busca = client.get('/livro/Livro Teste')
    id_livro = json.loads(busca.data)[0]["id"]
    rv = client.get('/livro/remover/{}'.format(id_livro), follow_redirects=True)
    assert b'Livro removido com sucesso!' in rv.data

def test_31_remover_ficha(client):
    busca = client.get('/ficha/12123234300')
    id_ficha = json.loads(busca.data)[0]["id"]
    rv = client.get('/ficha/remover/{}'.format(id_ficha), follow_redirects=True)
    assert b'Ficha removida com sucesso!' in rv.data

def test_99_logout(client):
    rv = logout(client)
    assert b'encerrada com sucesso!' in rv.data