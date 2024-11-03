# .github/scripts/test_homework4.py
import pytest
from httpx import AsyncClient, ASGITransport
from datetime import datetime, time, timedelta
from uuid import uuid4
from app.main import app

pytestmark = pytest.mark.anyio

async def test_filter_items():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.post(
            "/items/filter/",
            params={
                "price_min": 10,
                "price_max": 100,
                "tax_included": True,
                "tags": ["electronics", "home"]
            }
        )
    assert response.status_code == 200
    assert response.json() == {
        "price_range": [10, 100],
        "tax_included": True,
        "tags": ["electronics", "home"],
        "message": "This is a filtered list of items based on the provided criteria."
    }

async def test_create_item_with_fields():
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 19.99,
        "tax": 1.99
    }
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.post(
            "/items/create_with_fields/",
            json={"item": item_data, "importance": 5}
        )
    assert response.status_code == 200
    assert response.json() == {
        "item": item_data,
        "importance": 5
    }

async def test_create_offer():
    offer_data = {
        "name": "Special Offer",
        "discount": 15.5,
        "items": [
            {
                "name": "Item 1",
                "description": "First item",
                "price": 25.0,
                "tax": 2.5
            },
            {
                "name": "Item 2",
                "description": "Second item",
                "price": 30.0,
                "tax": 3.0
            }
        ]
    }
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.post("/offers/", json=offer_data)
    assert response.status_code == 200
    assert response.json() == {
        "offer_name": "Special Offer",
        "discount": 15.5,
        "items": offer_data["items"]
    }

async def test_create_user():
    user_data = {
        "username": "user123",
        "email": "user123@example.com",
        "full_name": "John Doe"
    }
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data

async def test_create_item_with_extra_data():
    extra_data = {
        "start_time": datetime.now().isoformat(),
        "end_time": time(23, 59, 59).isoformat(),
        "repeat_every": timedelta(days=1).total_seconds(),
        "process_id": str(uuid4())
    }
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.post("/items/extra_data_types/", json=extra_data)
    assert response.status_code == 200
    assert response.json()["message"] == "This is an item with extra data types."
    assert response.json()["process_id"] == extra_data["process_id"]

async def test_read_items_from_cookies():
    cookies = {"session_id": "test_session_id"}
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test", cookies=cookies) as ac:
        response = await ac.get("/items/cookies/")
    assert response.status_code == 200
    assert response.json() == {
        "session_id": "test_session_id",
        "message": "This is the session ID obtained from the cookies."
    }
