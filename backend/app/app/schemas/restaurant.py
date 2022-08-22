from typing import Optional

from pydantic import BaseModel


class RestaurantBase(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None


class RestaurantCreate(RestaurantBase):
    name: str
    address: str


class RestaurantUpdate(RestaurantBase):
    pass


class RestaurantInDBBase(RestaurantBase):
    id: Optional[int] = None

    class Config:
        orm_model = True


class Restaurant(RestaurantInDBBase):
    pass


class RestaurantInDB(RestaurantInDBBase):
    pass
