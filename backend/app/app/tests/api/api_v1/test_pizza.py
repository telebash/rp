from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.pizza import create_random_pizza


def test_create_pizza(
    client: TestClient, db: Session
) -> None:
    data = {"name": "Foo", "description": "Fighters"}
    response = client.post(
        f"{settings.API_V1_STR}/pizza/?restarant_id=1", json=data,
    )
    if response.status_code == 200:
        assert response.status_code == 200
        content = response.json()
        assert content["name"] == data["name"]
        assert content["description"] == data["description"]
        assert "id" in content
        assert "restaurant_id" in content
    else:
        assert response.status_code == 400


def test_read_pizza(
    client: TestClient,
    db: Session
) -> None:
    pizza = create_random_pizza(db)
    response = client.get(
        f"{settings.API_V1_STR}/pizza/{pizza.id}"
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == pizza.name
    assert content["description"] == pizza.description
    assert content["id"] == pizza.id
    assert content["restaurant_id"] == pizza.restaurant_id
