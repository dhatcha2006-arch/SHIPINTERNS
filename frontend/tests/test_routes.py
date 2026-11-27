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
    for route in ['/about', '/programs', '/contact', '/careers', '/internships']:
        response = client.get(route)
        assert response.status_code == 200
        assert b"SkillForge" in response.data

def test_auth_pages(client):
    for route in ['/auth/login', '/auth/register', '/auth/forgot-password']:
        response = client.get(route)
        assert response.status_code == 200
        assert b"SkillForge" in response.data

def test_student_dashboard(client):
    response = client.get('/student/dashboard')
    assert response.status_code == 200
    assert b"Internship Command Center" in response.data

def test_student_profile(client):
    response = client.get('/student/profile')
    assert response.status_code == 200
    assert b"Skill Passport" in response.data

def test_internship_application_flow(client):
    res1 = client.get('/student/apply')
    assert res1.status_code == 200
    assert b"Supervised Internship Application" in res1.data

    res2 = client.get('/student/application-status')
    assert res2.status_code == 200
    assert b"Application Status Tracker" in res2.data

def test_student_courses(client):
    response = client.get('/student/courses')
    assert response.status_code == 200
    assert b"Curriculum & Course Tracks" in response.data

    res2 = client.get('/student/courses/101')
    assert res2.status_code == 200
    assert b"Distributed RESTful Services" in res2.data

def test_student_roadmap(client):
    response = client.get('/student/roadmap')
    assert response.status_code == 200
    assert b"Interactive Learning Roadmap" in response.data

def test_student_lesson(client):
    response = client.get('/student/lesson')
    assert response.status_code == 200
    assert b"Connection Pooling" in response.data

def test_student_assignments(client):
    response = client.get('/student/assignments')
    assert response.status_code == 200
    assert b"Assignments & Code Deliverables" in response.data

def test_auth_api(client):
    res = client.post('/api/v1/auth/login', json={'email': 'alex.chen@skillforge.edu', 'password': 'test'})
    assert res.status_code == 200
    data = res.get_json()
    assert data['success'] is True
    assert 'token' in data
