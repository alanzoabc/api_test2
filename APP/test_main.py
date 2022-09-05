from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": True}

def test_get_account():
    response = client.get("/accounts/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Duck", "description": "quack", "balance": 2, "active": True}

def test_get_inexistent_account():
    response = client.get("/accounts/11")
    assert response.status_code == 404
    assert response.json() == { "detail":"Account not found"}


def test_create_account():
    response = client.put("/accounts/3", json={"name": "Dog", "description": "bark", "balance": 3.0, "active": True})
    assert response.status_code == 201
    assert response.json() == {"name": "Dog", "description": "bark", "balance": 3.0, "active": True}

def test_delete_account():
    response = client.delete("/accounts/1")
    assert response.status_code == 200
    assert response.json() == {"msg": "Successful"}