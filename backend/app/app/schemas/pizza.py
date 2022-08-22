from typing import Optional

from pydantic import BaseModel


class PizzaBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class PizzaCreate(PizzaBase):
    name: str
    description: str


class PizzaUpdate(PizzaBase):
    pass


class PizzaInDBBase(PizzaBase):
    id: int
    name: str
    description: str
    restaurant_id: int

    class Config:
        orm_model = True


class Pizza(PizzaInDBBase):
    pass


class PizzaInDB(PizzaInDBBase):
    pass
