from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/")
def read_restaurants(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Reteive restaurant
    """
    restaurant = crud.restaurant.get_multi(db, skip=skip, limit=limit)
    return restaurant


@router.post("/")
def create_restaurant(
    *,
    db: Session = Depends(deps.get_db),
    restarant_in: schemas.RestaurantCreate
) -> Any:
    """
    Create new restaurant.
    """
    restaurant = crud.restaurant.get_by_name(db, name=restarant_in.name)
    if restaurant:
        raise HTTPException(
            status_code=400,
            detail="This restaurant already exists in the system.",
        )
    restaurant = crud.restaurant.create(db, obj_in=restarant_in)
    return restaurant


@router.put("/{id}")
def update_restaurant(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    restaurant_in: schemas.RestaurantUpdate
) -> Any:
    """
    Update an restaurant.
    """
    restaurant = crud.restaurant.get(db=db, id=id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    restaurant = crud.restaurant.update(
        db=db,
        db_obj=restaurant,
        obj_in=restaurant_in
    )
    return restaurant


@router.get("/{id}")
def read_restaurant(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Get restaurant by ID.
    """
    restaurant = crud.restaurant.get(db=db, id=id)
    return restaurant


@router.delete("/{id}")
def delete_restaurant(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Delete an restaurant.
    """
    restaurant = crud.restaurant.get(db=db, id=id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    restaurant = crud.restaurant.remove(db=db, id=id)
    return restaurant
