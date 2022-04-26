import pytest

from src.domain.product import Product
from src.repository.products import RepositoryProducts


def test_repository_product():
    _product = RepositoryProducts()
    product = _product.get_product(pytest.QUOTES_MOCK)
    assert isinstance(product, Product)
