import enum
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


class CurrencysEnuns(enum.Enum):
    usd = "USDBRL"
    eur = "EURBRL"
    inr = "INRBRL"


class Prices(BaseModelCustom):
    def __init__(
        self, brl: Price, usd: Price = None, eur: Price = None, inr: Price = None
    ):
        self.brl = brl
        self.usd = usd
        self.eur = eur
        self.inr = inr

    @staticmethod
    def _convert_money(value: float, quote: float) -> float:
        return round(float(value) / float(quote), 2)

    def _price_model_coin(self, coin: str, quotes: Dict) -> Price:
        quote_coin = quotes[str(CurrencysEnuns[coin].value)]["ask"]

        return Price(
            price_of=self._convert_money(value=self.brl.price_of, quote=quote_coin),
            price_to=self._convert_money(value=self.brl.price_to, quote=quote_coin),
        )

    def calc_prices_country(self, quotes: Dict):
        self.usd = self._price_model_coin("usd", quotes)
        self.eur = self._price_model_coin("eur", quotes)
        self.inr = self._price_model_coin("inr", quotes)

    def to_dict(self) -> Dict:
        return dict(
            brl=self.brl.to_dict(),
            usd=self.usd.to_dict() if self.usd else None,
            eur=self.eur.to_dict() if self.eur else None,
            inr=self.inr.to_dict() if self.inr else None,
        )
