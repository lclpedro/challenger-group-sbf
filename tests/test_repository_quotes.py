import pytest
import requests_mock

from config import settings
from src.repository.quotes import RepositoryQuotes


def test_repository_quotes():
    with requests_mock.Mocker() as mocker:
        mocker.get(
            f"{settings.BASE_URL_SERVICE_QUOTE}/USD-BRL,EUR-BRL,INR-BRL",
            pytest.QUOTES_MOCK,
        )
        repo = RepositoryQuotes()
        assert isinstance(repo.get_quotes_coins(), dict)
