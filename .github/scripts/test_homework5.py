import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import status
try:
    from main import app  # Assuming the FastAPI application is in main.py
except ImportError:
    from app.main import app  # If unable to import from the main module, try importing from app.main

@pytest.mark.asyncio
async def test_create_item_with_form_and_file():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        form_data = {
            "name": "Test Item",
            "description": "A description for the test item",
            "price": 10.0,
            "tax": 2.0,
        }
        file_data = {
            "file": ("test_file.txt", "This is the content of the test file.", "text/plain")
        }

        response = await client.post("/items/form_and_file/", files=file_data, data=form_data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json["name"] == "Test Item"
    assert response_json["description"] == "A description for the test item"
    assert response_json["price"] == 10.0
    assert response_json["tax"] == 2.0
    assert response_json["filename"] == "test_file.txt"
    assert response_json["message"] == "This is an item created using form data and a file."


@pytest.mark.asyncio
async def test_create_item_with_negative_price():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        form_data = {
            "name": "Test Item",
            "description": "A description for the test item",
            "price": -10.0,
            "tax": 2.0,
        }
        file_data = {
            "file": ("test_file.txt", "This is the content of the test file.", "text/plain")
        }

        response = await client.post("/items/form_and_file/", files=file_data, data=form_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "Price cannot be negative"


@pytest.mark.asyncio
async def test_create_item_with_no_file():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        form_data = {
            "name": "Test Item",
            "description": "A description for the test item",
            "price": 10.0,
            "tax": 2.0,
        }

        response = await client.post("/items/form_and_file/", data=form_data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
