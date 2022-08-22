from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.pizza import Pizza
from app.schemas.pizza import PizzaCreate, PizzaUpdate


class CRUDPizza(CRUDBase[Pizza, PizzaCreate, PizzaUpdate]):
    def create_with_restaurant(
        self, db: Session, *, obj_in: PizzaCreate, restaurant_id: int
    ) -> Pizza:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, restaurant_id=restaurant_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_restaurant(
        self, db: Session, *, restaurant_id: int, skip: int = 0, limit: int = 100
    ) -> List[Pizza]:
        return (
            db.query(self.model)
            .filter(Pizza.restaurant_id == restaurant_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


pizza = CRUDPizza(Pizza)
