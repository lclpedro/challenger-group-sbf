from fastapi.routing import APIRouter

from .resources import products

router = APIRouter(prefix="/api/v1")

router.include_router(products)
