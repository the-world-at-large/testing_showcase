import json

from src.api import app


def test_ping():
    client = app.test_client()
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json == {"message": "pong"}


def test_sum_numbers():
    client = app.test_client()
    response = client.post("/sum", data=json.dumps({"a": 2, "b": 3}),
                           content_type="application/json")
    assert response.status_code == 200
    assert response.json == {"result": 5}
