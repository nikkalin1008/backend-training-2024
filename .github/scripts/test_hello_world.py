# .github/scripts/test_fastapi.py
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app object is in app.main

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}  # Adjust based on your FastAPI response
