from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .restaurant import Restaurant


class Pizza(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    restaurant = relationship("Restaurant", back_populates="pizza")
