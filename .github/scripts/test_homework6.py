from fastapi.testclient import TestClient
from datetime import datetime, time, timedelta
from uuid import uuid4
from main import app, Book, Author

client = TestClient(app)

def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["title"] == "Book 1"
    assert response.json()[1]["author"]["name"] == "Author 2"

def test_create_book_with_author():
    book_data = {
        "title": "New Book",
        "author": {
            "name": "New Author",
            "age": 40
        },
        "summary": "A brand new book about..."
    }
    response = client.post("/books/create_with_author/", json=book_data)
    assert response.status_code == 200
    assert response.json()["title"] == "New Book"
    assert response.json()["author"]["name"] == "New Author"
    assert response.json()["summary"] == "A brand new book about..."

def test_create_book():
    book_data = {
        "title": "Another Book",
        "author": {
            "name": "Another Author",
            "age": 50
        },
        "summary": "Another interesting story..."
    }
    response = client.post("/books/", json=book_data)
    assert response.status_code == 201
    assert response.json()["title"] == "Another Book"
    assert response.json()["author"]["name"] == "Another Author"
    assert response.json()["summary"] == "Another interesting story..."
