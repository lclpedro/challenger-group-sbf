from fastapi.routing import APIRouter

from .resources.products import products_router

router = APIRouter(prefix="/api/v1")

router.include_router(products_router)
