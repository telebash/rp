from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.restaurant import RestaurantCreate
from app.tests.utils.utils import random_lower_string


def create_random_restaurant(db: Session) -> models.Restaurant:
    name = random_lower_string()
    address = random_lower_string()
    restaurant_in = RestaurantCreate(name=name, address=address)
    return crud.restaurant.create(db=db, obj_in=restaurant_in)
