import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_health(client):
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"SkillForge" in response.data
    assert b"Where Academic Foundations Meet Supervised Industry Practice" in response.data

def test_public_pages(client):
    for route in ['/about', '/programs', '/contact', '/careers']:
        response = client.get(route)
        assert response.status_code == 200
        assert b"SkillForge" in response.data
