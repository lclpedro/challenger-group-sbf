from typing import Dict

from src.repository.products import RepositoryProducts
from src.repository.quotes import RepositoryQuotes
from src.schemas.product import ProductSchema


class ServiceProducts:
    def __init__(
        self,
        repository_quotes: RepositoryQuotes,
        repository_product: RepositoryProducts,
    ):
        self.repository_quotes = repository_quotes
        self.repository_product = repository_product

    def _get_quotes_coins(self) -> Dict:
        quotes = self.repository_quotes.get_quotes_coins()
        return quotes

    def get_a_product(self) -> ProductSchema:
        product = self.repository_product.get_product()
        return product
