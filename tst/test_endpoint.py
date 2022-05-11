from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_predict():
    response = client.post("/predict/", json={
        "name": "Heck",
        "id": 42
    })

    assert response.status_code == 200
    assert response.json()["prediction"] == 420
