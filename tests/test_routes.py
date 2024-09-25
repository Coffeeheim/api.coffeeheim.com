from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_permittedlist():
    response = client.post('/permittedlist')
    assert response.status_code == HTTPStatus.CREATED


def test_status():
    response = client.get('/status')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {}
