import pytest
from flask import escape
from users.models import db, User
from app import app  # הנח שהאפליקציה שלך נמצאת ב-app.py


@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
    client = app.test_client()

    yield client  # מה שיחזור לטסטים

    with app.app_context():
        db.session.remove()
        db.drop_all()


def test_create_user(client):
    response = client.post('/', json={
        'name': 'John Doe',
        'age': 30,
        'group': 'Developers'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'John Doe'
    assert data['age'] == '30'
    assert data['group'] == 'Developers'


def test_get_users(client):
    # יצירת משתמש לבדיקה
    client.post('/', json={
        'name': 'John Doe',
        'age': 30,
        'group': 'Developers'
    })
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['name'] == 'John Doe'


def test_get_user(client):
    # יצירת משתמש לבדיקה
    client.post('/', json={
        'name': 'John Doe',
        'age': 30,
        'group': 'Developers'
    })
    response = client.get('/1')  # משתמש עם ID=1
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'John Doe'


def test_get_nonexistent_user(client):
    response = client.get('/999')  # משתמש שלא קיים
    assert response.status_code == 404


def test_update_user(client):
    # יצירת משתמש לבדיקה
    client.post('/', json={
        'name': 'John Doe',
        'age': 30,
        'group': 'Developers'
    })
    # עדכון המשתמש
    response = client.put('/1', json={
        'name': 'Jane Doe',
        'age': 25,
        'group': 'Managers'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Jane Doe'
    assert data['age'] == '25'
    assert data['group'] == 'Managers'

def test_delete_user(client):
    # יצירת משתמש לבדיקה
    client.post('/', json={
        'name': 'John Doe',
        'age': 30,
        'group': 'Developers'
    })
    # מחיקת המשתמש
    response = client.delete('/1')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'User deleted'}


def test_delete_nonexistent_user(client):
    response = client.delete('/999')  # ניסיון למחוק משתמש שלא קיים
    assert response.status_code == 404