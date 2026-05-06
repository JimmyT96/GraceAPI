import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.json['service'] == 'GraceAPI'
    assert res.json['author'] == 'Jemimah'

def test_health(client):
    res = client.get('/api/v1/health')
    assert res.status_code == 200
    assert res.json['status'] == 'healthy'

def test_random_verse(client):
    res = client.get('/api/v1/verse')
    assert res.status_code == 200
    assert 'reference' in res.json['data']
