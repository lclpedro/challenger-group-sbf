from typing import Dict

from src.domain import BaseModelCustom
from src.domain.prices import Prices


class Product(BaseModelCustom):
    def __init__(self, name: str, image: str, prices: Prices):
        self.name = name
        self.image = image
        self.prices = prices

    def to_dict(self) -> Dict:
        return dict(name=self.name, image=self.image, prices=self.prices.to_dict())
