from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.restaurant import create_random_restaurant


def test_create_restaurant(
    client: TestClient, db: Session
) -> None:
    data = {"name": "Foo", "address": "Fighters"}
    response = client.post(
        f"{settings.API_V1_STR}/restaurant/", json=data,
    )
    if response.status_code == 200:
        assert response.status_code == 200
        content = response.json()
        assert content["name"] == data["name"]
        assert content["address"] == data["address"]
        assert "id" in content
    else:
        assert response.status_code == 400


def test_read_restaurant(
    client: TestClient,
    db: Session
) -> None:
    restaurant = create_random_restaurant(db)
    response = client.get(
        f"{settings.API_V1_STR}/restaurant/{restaurant.id}"
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == restaurant.name
    assert content["address"] == restaurant.address
    assert content["id"] == restaurant.id
