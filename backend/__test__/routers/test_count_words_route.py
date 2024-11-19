from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

endpoint = "/word/"

def test_count_word_valid_request():
    response = client.post(endpoint, json={"text": "Text input"})
    json_response = response.json()

    assert response.status_code == 200
    assert json_response.get("number") == 2


def test_count_word_error_request():
    response = client.post(endpoint, json={"text": ""})
    json_response = response.json()

    assert response.status_code == 400
    assert json_response["detail"]["message"] == "Text input is required!"