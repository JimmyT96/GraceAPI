import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get('/')
    assert res.status_code == 200

def test_get_verses(client):
    res = client.get('/verses')
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_get_verse_by_id(client):
    res = client.get('/verses/1')
    assert res.status_code == 200
    assert 'id' in res.json
