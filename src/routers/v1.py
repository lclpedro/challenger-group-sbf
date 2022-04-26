from fastapi.routing import APIRouter

from .resources.products import products_router

router = APIRouter(prefix="/v1")

router.include_router(products_router)
