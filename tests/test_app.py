from fastapi.testclient import TestClient
from fast_zero.app import app
from http import HTTPStatus

def test_read_root():
    client = TestClient(app)
    
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}