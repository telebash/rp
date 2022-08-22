from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .pizza import Pizza


class Restaurant(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    pizza = relationship("Pizza", back_populates="restaurant")
