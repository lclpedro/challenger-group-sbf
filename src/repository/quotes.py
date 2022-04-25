import logging
from typing import Any, Dict, List

import requests

from config import settings

_logger = logging.getLogger(__name__)


class RepositoryQuotes:
    def __init__(
        self,
        base_url_service_quote: str = settings.base_url_service_quote,
        coin_default: str = settings.coin_default,
        coins_enabled: List = settings.coins_enabled,
        logger=_logger,
    ):
        self.base_url_service_quote = base_url_service_quote
        self.coin_default = coin_default
        self.coins_enabled = coins_enabled
        self.logger = logger

    def _mount_pairs_coins(self) -> str:
        str_coins = ""
        for coin in self.coins_enabled:
            str_coins += f"{coin}-{self.coin_default},"
        self.logger.debug(f"Pairs Coins: {str_coins}")
        return str_coins[:-1]

    def get_quotes_coins(self) -> Dict[str, Any]:
        _quotes = requests.get(
            f"{self.base_url_service_quote}/{self._mount_pairs_coins()}"
        )
        self.logger.info(
            f"[RepositoryQuotes] = StatusCode request service quotes: {_quotes.status_code}"
        )

        if _quotes.status_code is not requests.codes.OK:
            _quotes.raise_for_status()

        quotes = _quotes.json()
        self.logger.debug(f"Response Quotes: {quotes}")
        return quotes
