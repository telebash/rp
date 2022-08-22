from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/")
def read_pizzas(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Reteive Pizza
    """
    pizza = crud.pizza.get_multi(db, skip=skip, limit=limit)
    return pizza


@router.post("/")
def create_pizza(
    *,
    db: Session = Depends(deps.get_db),
    pizza_in: schemas.PizzaCreate,
    restarant_id: int
) -> Any:
    """
    Create new pizza.
    """
    pizza = crud.pizza.create_with_restaurant(
        db=db,
        obj_in=pizza_in,
        restaurant_id=restarant_id
    )
    return pizza


@router.put("/{id}")
def update_pizza(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    pizza_in: schemas.PizzaUpdate
) -> Any:
    """
    Update an pizza.
    """
    pizza = crud.pizza.get(db=db, id=id)
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    pizza = crud.pizza.update(db=db, db_obj=pizza, obj_in=pizza_in)
    return pizza


@router.get("/{id}")
def read_pizza(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Get pizza by ID.
    """
    pizza = crud.pizza.get(db=db, id=id)
    return pizza


@router.delete("/{id}")
def delete_pizza(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Delete an pizza.
    """
    pizza = crud.pizza.get(db=db, id=id)
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    pizza = crud.pizza.remove(db=db, id=id)
    return pizza
