from sqlalchemy.orm import Session

from app import crud
from app.schemas.pizza import PizzaCreate, PizzaUpdate
from app.tests.utils.restaurant import create_random_restaurant
from app.tests.utils.utils import random_lower_string


def test_create_pizza(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    pizza_in = PizzaCreate(name=name, description=description)
    restaurant = create_random_restaurant(db)
    pizza = crud.pizza.create_with_restaurant(
        db=db,
        obj_in=pizza_in,
        restaurant_id=restaurant.id
    )
    assert pizza.name == name
    assert pizza.description == description
    assert pizza.restaurant_id == restaurant.id


def test_get_pizza(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    pizza_in = PizzaCreate(name=name, description=description)
    restaurant = create_random_restaurant(db)
    pizza = crud.pizza.create_with_restaurant(
        db=db,
        obj_in=pizza_in,
        restaurant_id=restaurant.id
    )
    stored_pizza = crud.pizza.get(db=db, id=pizza.id)
    assert stored_pizza
    assert pizza.id == stored_pizza.id
    assert pizza.name == stored_pizza.name
    assert pizza.description == stored_pizza.description
    assert pizza.restaurant_id == stored_pizza.restaurant_id


def test_update_pizza(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    pizza_in = PizzaCreate(name=name, description=description)
    restaurant = create_random_restaurant(db)
    pizza = crud.pizza.create_with_restaurant(
        db=db,
        obj_in=pizza_in,
        restaurant_id=restaurant.id
    )
    description2 = random_lower_string()
    pizza_update = PizzaUpdate(description=description2)
    pizza2 = crud.pizza.update(db=db, db_obj=pizza, obj_in=pizza_update)
    assert pizza.id == pizza2.id
    assert pizza.name == pizza2.name
    assert pizza2.description == description2
    assert pizza.restaurant_id == pizza2.restaurant_id


def test_delete_item(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    pizza_in = PizzaCreate(name=name, description=description)
    restaurant = create_random_restaurant(db)
    pizza = crud.pizza.create_with_restaurant(
        db=db,
        obj_in=pizza_in,
        restaurant_id=restaurant.id
    )
    pizza2 = crud.pizza.remove(db=db, id=pizza.id)
    pizza3 = crud.pizza.get(db=db, id=pizza.id)
    assert pizza3 is None
    assert pizza2.id == pizza.id
    assert pizza2.name == name
    assert pizza2.description == description
    assert pizza2.restaurant_id == restaurant.id
