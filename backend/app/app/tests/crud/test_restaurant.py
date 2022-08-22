from sqlalchemy.orm import Session

from app import crud
from app.schemas.restaurant import RestaurantCreate, RestaurantUpdate
from app.tests.utils.utils import random_lower_string


def test_create_restaurant(db: Session) -> None:
    name = random_lower_string()
    address = random_lower_string()
    restaurant_in = RestaurantCreate(name=name, address=address)
    restaurant = crud.restaurant.create(
        db=db,
        obj_in=restaurant_in
    )
    assert restaurant.name == name
    assert restaurant.address == address


def test_get_pizza(db: Session) -> None:
    name = random_lower_string()
    address = random_lower_string()
    restaurant_in = RestaurantCreate(name=name, address=address)
    restaurant = crud.restaurant.create(
        db=db,
        obj_in=restaurant_in
    )
    stored_restaurant = crud.restaurant.get(db=db, id=restaurant.id)
    assert stored_restaurant
    assert restaurant.id == stored_restaurant.id
    assert restaurant.name == stored_restaurant.name
    assert restaurant.address == stored_restaurant.address


def test_update_pizza(db: Session) -> None:
    name = random_lower_string()
    address1 = random_lower_string()
    restaurant_in = RestaurantCreate(name=name, address=address1)
    restaurant = crud.restaurant.create(
        db=db,
        obj_in=restaurant_in
    )
    address2 = random_lower_string()
    restaurant_update = RestaurantUpdate(address=address2)
    restaurant2 = crud.restaurant.update(
        db=db,
        db_obj=restaurant,
        obj_in=restaurant_update
    )
    assert restaurant.id == restaurant2.id
    assert restaurant.name == restaurant2.name
    assert restaurant2.address == address2


def test_delete_item(db: Session) -> None:
    name = random_lower_string()
    address = random_lower_string()
    restaurant_in = RestaurantCreate(name=name, address=address)
    restaurant = crud.restaurant.create(
        db=db,
        obj_in=restaurant_in
    )
    restaurant2 = crud.restaurant.remove(db=db, id=restaurant.id)
    restaurant3 = crud.restaurant.get(db=db, id=restaurant.id)
    assert restaurant3 is None
    assert restaurant2.id == restaurant.id
    assert restaurant2.name == name
    assert restaurant2.address == address
