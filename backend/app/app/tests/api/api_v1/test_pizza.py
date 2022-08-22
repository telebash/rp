from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.pizza import create_random_pizza
from app.tests.utils.pizza import delete_pizza
from app.tests.utils.restaurant import create_random_restaurant
from app.tests.utils.utils import random_lower_string


def test_create_pizza(
    client: TestClient, db: Session
) -> None:
    restaurant = create_random_restaurant(db)
    data = {
        "name": random_lower_string(),
        "description": random_lower_string()
    }
    response = client.post(
        f"{settings.API_V1_STR}/pizza/?restarant_id={restaurant.id}",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert "id" in content
    assert content["name"] == data["name"]
    assert content["description"] == data["description"]
    assert content["restaurant_id"] == restaurant.id


def test_read_pizzas(
    client: TestClient,
    db: Session
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/pizza/"
    )
    assert response.status_code == 200
    content = response.json()
    for pizza in content:
        assert "id" in pizza
        assert "name" in pizza
        assert "description" in pizza
        assert "restaurant_id" in pizza


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


def test_update_pizza(
    client: TestClient,
    db: Session
) -> None:
    pizza = create_random_pizza(db)
    data = {
        "description": random_lower_string()
    }
    response = client.put(
        f"{settings.API_V1_STR}/pizza/{pizza.id}", json=data
    )
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == pizza.id
    assert content["name"] == pizza.name
    assert content["description"] == data["description"]
    assert content["restaurant_id"] == pizza.restaurant_id


def test_update_not_found_pizza(
    client: TestClient,
    db: Session
) -> None:
    pizza = create_random_pizza(db)
    delete_pizza(db=db, id=pizza.id)
    data = {
        "description": random_lower_string()
    }
    response = client.put(
        f"{settings.API_V1_STR}/pizza/{pizza.id}", json=data
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Pizza not found"


def test_delete_pizza(
    client: TestClient,
    db: Session
) -> None:
    pizza = create_random_pizza(db)
    response = client.delete(
        f"{settings.API_V1_STR}/pizza/{pizza.id}"
    )
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == pizza.id
    assert content["name"] == pizza.name
    assert content["description"] == pizza.description
    assert content["restaurant_id"] == pizza.restaurant_id


def test_delete_not_found_pizza(
    client: TestClient,
    db: Session
) -> None:
    pizza = create_random_pizza(db)
    delete_pizza(db=db, id=pizza.id)
    response = client.delete(
        f"{settings.API_V1_STR}/pizza/{pizza.id}"
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Pizza not found"
