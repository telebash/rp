from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.restaurant import create_random_restaurant
from app.tests.utils.restaurant import delete_restaurant
from app.tests.utils.utils import random_lower_string


def test_create_restaurant(
    client: TestClient,
    db: Session
) -> None:
    data = {
        "name": random_lower_string(),
        "address": random_lower_string()
    }
    response = client.post(
        f"{settings.API_V1_STR}/restaurant/", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["address"] == data["address"]
    assert "id" in content


def test_create_restaurant_exc(
    client: TestClient,
    db: Session
) -> None:
    restaurant = create_random_restaurant(db)
    data = {
        "name": restaurant.name,
        "address": restaurant.address
    }
    response = client.post(
        f"{settings.API_V1_STR}/restaurant/", json=data,
    )
    assert response.status_code == 400
    content = response.json()
    assert content["detail"] == "This restaurant already exists in the system."


def test_read_restaurants(
    client: TestClient,
    db: Session
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/restaurant/"
    )
    assert response.status_code == 200
    content = response.json()
    for restaurant in content:
        assert "id" in restaurant
        assert "name" in restaurant
        assert "address" in restaurant


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


def test_update_restaurant(
    client: TestClient,
    db: Session
) -> None:
    restaurant = create_random_restaurant(db)
    data = {
        "address": random_lower_string()
    }
    response = client.put(
        f"{settings.API_V1_STR}/restaurant/{restaurant.id}", json=data
    )
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == restaurant.id
    assert content["name"] == restaurant.name
    assert content["address"] == data["address"]


def test_update_not_found_restaurant(
    client: TestClient,
    db: Session
) -> None:
    restaurant = create_random_restaurant(db)
    delete_restaurant(db=db, id=restaurant.id)
    data = {
        "address": random_lower_string()
    }
    response = client.put(
        f"{settings.API_V1_STR}/restaurant/{restaurant.id}", json=data
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Restaurant not found"


def test_delete_restaurant(
    client: TestClient,
    db: Session
) -> None:
    restaurant = create_random_restaurant(db)
    response = client.delete(
        f"{settings.API_V1_STR}/restaurant/{restaurant.id}"
    )
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == restaurant.id
    assert content["name"] == restaurant.name
    assert content["address"] == restaurant.address


def test_delete_not_found_pizza(
    client: TestClient,
    db: Session
) -> None:
    restaurant = create_random_restaurant(db)
    delete_restaurant(db=db, id=restaurant.id)
    response = client.delete(
        f"{settings.API_V1_STR}/restaurant/{restaurant.id}"
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Restaurant not found"
