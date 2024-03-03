from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"app_name": "Notes-Scribe"}


def test_read_chat_with_llm():
    response = client.get("/chat_with_llm?prompt=who%20is%20naruto")
    assert response.status_code == 200


def test_read_chat_with_knowledge_base():
    response = client.get("/chat_with_knowledge_base?prompt=what%20is%20agile")
    assert response.status_code == 200
