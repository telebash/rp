from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.pizza import PizzaCreate
from app.tests.utils.restaurant import create_random_restaurant
from app.tests.utils.utils import random_lower_string


def create_random_pizza(
    db: Session,
    *,
    restaurant_id: Optional[int] = None
) -> models.Pizza:
    if restaurant_id is None:
        restaurant = create_random_restaurant(db)
        restaurant_id = restaurant.id
    name = random_lower_string()
    description = random_lower_string()
    pizza_in = PizzaCreate(name=name, description=description, id=id)
    return crud.pizza.create_with_restaurant(
        db=db,
        obj_in=pizza_in,
        restaurant_id=restaurant_id
    )
