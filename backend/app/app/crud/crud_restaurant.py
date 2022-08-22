from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.restaurant import Restaurant
from app.schemas.restaurant import RestaurantCreate, RestaurantUpdate


class CRUDRestaurant(CRUDBase[Restaurant, RestaurantCreate, RestaurantUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Restaurant]:
        return db.query(Restaurant).filter(Restaurant.name == name).first()

    def create(self, db: Session, *, obj_in: RestaurantCreate) -> Restaurant:
        db_obj = Restaurant(
            name=obj_in.name,
            address=obj_in.address
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Restaurant,
        obj_in: Union[RestaurantUpdate, Dict[str, Any]]
    ) -> Restaurant:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


restaurant = CRUDRestaurant(Restaurant)
