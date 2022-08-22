from fastapi import APIRouter

from app.api.api_v1.endpoints import pizza, restaurant

api_router = APIRouter()
api_router.include_router(pizza.router, prefix="/pizza", tags=["pizza"])
api_router.include_router(restaurant.router, prefix="/restaurant", tags=["restaurant"])
