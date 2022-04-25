from fastapi import APIRouter

from repository.products import RepositoryProducts
from src.repository.quotes import RepositoryQuotes
from src.schemas.product import ProductSchema
from src.services.products import ServiceProducts

products_router = APIRouter(prefix="/products", tags=["Products"])


@products_router.get("/", response_model=ProductSchema)
def router_products():
    RepositoryQuotes
    service_product = ServiceProducts(
        repository_quotes=RepositoryQuotes(), repository_product=RepositoryProducts()
    )
    return service_product.get_a_product()
