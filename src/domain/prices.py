from typing import Dict

from src.domain import BaseModelCustom


class Price(BaseModelCustom):
    def __init__(self, price_of: float, price_to: float):
        self.price_of = price_of
        self.price_to = price_to
        self.percent_discount = self._calculate_percent_off()

    def _calculate_percent_off(self) -> int:
        return int(((self.price_to / self.price_of) - 1) * 100)

    def to_dict(self) -> Dict:
        return dict(
            price_of=self.price_of,
            price_to=self.price_to,
            percent_discount=self.percent_discount,
        )


class Prices(BaseModelCustom):
    def __init__(
        self, brl: Price, usd: Price = None, eur: Price = None, inr: Price = None
    ):
        self.brl = brl
        self.usd = usd
        self.eur = eur
        self.inr = inr

    # TODO: Definir como será realizado o encapsulamento de novas moedas, talvez criar uma factory.

    def to_dict(self) -> Dict:
        return dict(
            brl=self.brl.to_dict(),
            usd=self.usd.to_dict(),
            eur=self.eur.to_dict(),
            inr=self.inr.to_dict(),
        )
