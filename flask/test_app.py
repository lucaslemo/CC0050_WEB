from app import app
import pytest

aplicacao = app.test_client()

@pytest.fixture
def client():
    return (aplicacao)

def test_0_index(client):
    rv = client.get('/')
    assert 500 != rv.status_code