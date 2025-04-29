from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "XP Inc. - Migrador de Dados"}

def test_migrar():
    response = client.post("/migrar")
    assert response.status_code == 200
    assert "concluída" in response.json()["status"]