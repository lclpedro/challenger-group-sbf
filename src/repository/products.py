from typing import Dict

from src.domain.prices import Price, Prices
from src.domain.product import Product

product_mock = dict(
    name="Tênis Nike Shox R4 - Masculino",
    image="https://images.lojanike.com.br/500x500/produto/tenis-nike-shox-r4-masculino-104265-045-1-11643055673.jpg",
    price_of=749.99,
    price_to=529.99,
)


class RepositoryProducts:
    def __init__(self, product=product_mock):
        self.product = product

    def get_product(self, quotes: Dict) -> Product:
        product = Product(
            name=self.product["name"],
            image=self.product["image"],
            prices=Prices(
                brl=Price(
                    price_of=self.product["price_of"], price_to=self.product["price_to"]
                )
            ),
        )
        product.prices.calc_prices_country(quotes=quotes)
        return product
