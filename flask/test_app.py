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
    rv = login(client, 'admin', '123456')
    assert b'autenticado com sucesso!' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_4_usuario_cadastrar_username_errado(client):
    data = dict(nome='Nome Teste',
                username='admin',
                email='email_teste@email.com',
                telefone='+55 (88)9999-9999',
                senha='senha_teste123',
                admin='n')
    rv = client.post('/usuario/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'rio cadastrado com esse Nome de usu' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_5_usuario_cadastrar_email_errado(client):
    data = dict(nome='Nome Teste',
                username='usertest',
                email='admin@biblioteca.com',
                telefone='+55 (88)9999-9999',
                senha='senha_teste123',
                admin='n')
    rv = client.post('/usuario/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'rio cadastrado com esse Nome de usu' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_5_usuario_cadastrar_email_errado(client):
    data = dict(nome='Nome Teste',
                username='usertest',
                email='admin@biblioteca.com',
                telefone='+55 (88)9999-9999',
                senha='senha_teste123',
                admin='n')
    rv = client.post('/usuario/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'rio cadastrado com esse Nome de usu' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_6_usuario_cadastrar_01(client):
    data = dict(nome='Nome Teste',
                username='usertest01',
                email='usertest01@biblioteca.com',
                telefone='+55 (88)9999-9999',
                senha='senha_teste123',
                admin='n')
    rv = client.post('/usuario/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'rio cadastrado com sucesso!' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_7_usuario_cadastrar_02(client):
    data = dict(nome='Nome Teste',
                username='usertest02',
                email='usertest02@biblioteca.com',
                telefone='+55 (88)9999-9999',
                senha='senha_teste123',
                admin='n')
    rv = client.post('/usuario/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'rio cadastrado com sucesso!' in rv.data

def test_8_usuario_listar(client):
    rv = client.get('/usuario/listar', follow_redirects=True)
    assert b'ID' in rv.data
    assert b'Nome de Usu' in rv.data
    assert b'E-mail' in rv.data
    assert b'Administrador' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_9_novo_login(client):
    rv = login(client, 'usertest01', 'senha_teste123')
    assert b'autenticado com sucesso!' in rv.data

def test_10_usuario_listar_errado(client):
    rv = client.get('/usuario/listar', follow_redirects=True)
    assert b'Apenas administradores podem listar os usu' in rv.data

def test_11_remover_usuario_errado(client):
    busca = client.get('/usuario/usertest02')
    id_usuario = json.loads(busca.data)[0]["id"]
    rv = client.get('/usuario/remover/{}'.format(id_usuario), follow_redirects=True)
    assert b'Apenas administradores podem remover usu' in rv.data

def test_12_livro_listar(client):
    rv = client.get('/livro/listar', follow_redirects=True)
    assert b'ID' in rv.data
    assert b'tulo' in rv.data
    assert b'Autor' in rv.data
    assert b'Dispon' in rv.data

def test_13_ficha_listar(client):
    rv = client.get('/ficha/listar', follow_redirects=True)
    assert b'ID' in rv.data
    assert b'Nome' in rv.data
    assert b'CPF' in rv.data
    assert b'Livros Lidos' in rv.data

def test_14_emprestimos_listar(client):
    rv = client.get('/emprestimo/listar', follow_redirects=True)
    assert b'ID' in rv.data
    assert b'Respons' in rv.data
    assert b'Dono da Ficha' in rv.data
    assert b'Data do Empr' in rv.data

def test_15_livro_json(client):
    rv = client.get('/livro/listar/json')
    assert 500 != rv.status_code

def test_16_usuario_json(client):
    rv = client.get('/usuario/listar/json')
    assert 500 != rv.status_code

def test_17_emprestimo_json(client):
    rv = client.get('/emprestimo/listar/json')
    assert 500 != rv.status_code

def test_18_ficha_json(client):
    rv = client.get('/ficha/listar/json')
    assert 500 != rv.status_code

def test_19_busca_livro_nao_existente(client):
    rv = client.get('/livro/livro_nao_existente')
    assert 500 != rv.status_code

def test_20_busca_usuario_nao_existente(client):
    rv = client.get('/usuario/usuario_nao_existente')
    assert 500 != rv.status_code

def test_21_busca_emprestimo_nao_existente(client):
    rv = client.get('/emprestimo/0/0')
    assert 500 != rv.status_code

def test_22_busca_livro_nao_existente(client):
    rv = client.get('/ficha/ficha_nao_existente')
    assert 500 != rv.status_code

@pytest.mark.usefixtures('preparacao')
def test_23_livro_cadastrar(client):
    data = dict(titulo='Livro Teste',
                autor='Autor Teste',
                genero='Genero Teste')
    rv = client.post('/livro/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'Livro cadastrado com sucesso!' in rv.data

def test_24_busca_livro(client):
    rv = client.get('/livro/Livro Teste')
    assert 500 != rv.status_code

def test_25_busca_livro_upper(client):
    rv = client.get('/livro/livro teste')
    assert b'Livro Teste' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_26_ficha_cadastrar(client):
    data = dict(nome='Nome Teste',
                cpf='12123234300',
                email='teste@email.com')
    rv = client.post('/ficha/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'Ficha cadastrada com sucesso!' in rv.data

def test_27_busca_ficha(client):
    rv = client.get('/ficha/12123234300')
    assert 500 != rv.status_code

def test_28_busca_ficha_upper(client):
    rv = client.get('/ficha/12123234300')
    assert b'Nome Teste' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_29_ficha_cadastrar_repetido_cpf(client):
    data = dict(nome='Outro Nome Teste',
                cpf='12123234300',
                email='outro_teste@email.com')
    rv = client.post('/ficha/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'ficha cadastrada com esse E-mail ou CPF' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_30_ficha_cadastrar_repetido_email(client):
    data = dict(nome='Outro Nome Teste',
                cpf='00100200341',
                email='teste@email.com')
    rv = client.post('/ficha/cadastrar',
                        data=data,
                        follow_redirects=True)
    assert b'ficha cadastrada com esse E-mail ou CPF' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_31_emprestimo(client):
    busca_ficha = client.get('/ficha/12123234300')
    id_ficha = json.loads(busca_ficha.data)[0]["id"]
    busca_livro = client.get('/livro/Livro Teste')
    id_livro = json.loads(busca_livro.data)[0]["id"]
    data = dict(ficha=int('{}'.format(id_ficha)),
                livro=int('{}'.format(id_livro)))
    rv = client.post('/emprestimo',
                        data=data,
                        follow_redirects=True)
    assert b'stimo realizado com sucesso!' in rv.data

def test_32_remover_livro_errado(client):
    busca = client.get('/livro/Livro Teste')
    id_livro = json.loads(busca.data)[0]["id"]
    rv = client.get('/livro/remover/{}'.format(id_livro), follow_redirects=True)
    assert b'Apenas administradores podem remover livros!' in rv.data

def test_33_remover_ficha_errado(client):
    busca = client.get('/ficha/12123234300')
    id_ficha = json.loads(busca.data)[0]["id"]
    rv = client.get('/ficha/remover/{}'.format(id_ficha), follow_redirects=True)
    assert b'Apenas administradores podem remover fichas!' in rv.data

@pytest.mark.usefixtures('preparacao')
def test_34_novo_login(client):
    rv = login(client, 'admin', '123456')
    assert b'autenticado com sucesso!' in rv.data

def test_35_remover_usuario_admin_errado(client):
    busca = client.get('/usuario/admin')
    id_usuario = json.loads(busca.data)[0]["id"]
    rv = client.get('/usuario/remover/{}'.format(id_usuario), follow_redirects=True)
    assert b'rio logado na sess' in rv.data

def test_36_remover_usuario_01(client):
    busca = client.get('/usuario/usertest01')
    id_usuario = json.loads(busca.data)[0]["id"]
    rv = client.get('/usuario/remover/{}'.format(id_usuario), follow_redirects=True)
    assert b'rio removido com sucesso!' in rv.data

def test_37_remover_usuario_02(client):
    busca = client.get('/usuario/usertest02')
    id_usuario = json.loads(busca.data)[0]["id"]
    rv = client.get('/usuario/remover/{}'.format(id_usuario), follow_redirects=True)
    assert b'rio removido com sucesso!' in rv.data

def test_38_remover_livro_nao_devolvido(client):
    busca = client.get('/livro/Livro Teste')
    id_livro = json.loads(busca.data)[0]["id"]
    rv = client.get('/livro/remover/{}'.format(id_livro), follow_redirects=True)
    assert b'O livro precisa estar dispon' in rv.data

def test_39_remover_ficha_com_livros(client):
    busca = client.get('/ficha/12123234300')
    id_ficha = json.loads(busca.data)[0]["id"]
    rv = client.get('/ficha/remover/{}'.format(id_ficha), follow_redirects=True)
    assert b'O leitor possui livros n' in rv.data

def test_40_remover_emprestimo_nao_devolvido(client):
    busca_ficha = client.get('/ficha/12123234300')
    id_ficha = json.loads(busca_ficha.data)[0]["id"]
    busca_livro = client.get('/livro/Livro Teste')
    id_livro = json.loads(busca_livro.data)[0]["id"]
    buscar_emprestimo = client.get('/emprestimo/{}/{}'.format(id_ficha, id_livro), follow_redirects=True)
    id_emprestimo = json.loads(buscar_emprestimo.data)[0]["id"]
    rv = client.get('/emprestimo/remover/{}'.format(id_emprestimo), follow_redirects=True)
    assert b'O livro precisa ser devolvido antes da remo' in rv.data

def test_41_devolver_remover_emprestimo(client):
    busca_ficha = client.get('/ficha/12123234300')
    id_ficha = json.loads(busca_ficha.data)[0]["id"]
    busca_livro = client.get('/livro/Livro Teste')
    id_livro = json.loads(busca_livro.data)[0]["id"]
    buscar_emprestimo = client.get('/emprestimo/{}/{}'.format(id_ficha, id_livro), follow_redirects=True)
    id_emprestimo = json.loads(buscar_emprestimo.data)[0]["id"]
    rv01 = client.get('/livro/devolver/{}'.format(id_emprestimo), follow_redirects=True)
    rv02 = client.get('/emprestimo/remover/{}'.format(id_emprestimo), follow_redirects=True)
    assert b'Livro devolvido com sucesso!' in rv01.data
    assert b'stimo removida com sucesso!' in rv02.data

def test_42_remover_livro(client):
    busca = client.get('/livro/Livro Teste')
    id_livro = json.loads(busca.data)[0]["id"]
    rv = client.get('/livro/remover/{}'.format(id_livro), follow_redirects=True)
    assert b'Livro removido com sucesso!' in rv.data

def test_43_remover_ficha(client):
    busca = client.get('/ficha/12123234300')
    id_ficha = json.loads(busca.data)[0]["id"]
    rv = client.get('/ficha/remover/{}'.format(id_ficha), follow_redirects=True)
    assert b'Ficha removida com sucesso!' in rv.data

def test_44_logout(client):
    rv = logout(client)
    assert b'encerrada com sucesso!' in rv.data