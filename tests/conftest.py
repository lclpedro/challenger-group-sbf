import os

import pytest

os.environ["SBF_ENVIRONMENT"] = "tester"

quotes_mock = {
    "USDBRL": {
        "code": "USD",
        "codein": "BRL",
        "name": "Dólar Americano/Real Brasileiro",
        "high": "4.8382",
        "low": "4.6214",
        "varBid": "0.174",
        "pctChange": "3.76",
        "bid": "4.7955",
        "ask": "4.7965",
        "timestamp": "1650661194",
        "create_date": "2022-04-22 17:59:54",
    },
    "EURBRL": {
        "code": "EUR",
        "codein": "BRL",
        "name": "Euro/Real Brasileiro",
        "high": "5.1857",
        "low": "5.1766",
        "varBid": "0.0057",
        "pctChange": "0.11",
        "bid": "5.1777",
        "ask": "5.1823",
        "timestamp": "1650846465",
        "create_date": "2022-04-24 21:27:45",
    },
    "INRBRL": {
        "code": "INR",
        "codein": "BRL",
        "name": "Rúpia Indiana/Real Brasileiro",
        "high": "0.06272",
        "low": "0.06272",
        "varBid": "-0.00007",
        "pctChange": "-0.11",
        "bid": "0.06272",
        "ask": "0.06273",
        "timestamp": "1650846368",
        "create_date": "2022-04-24 21:26:08",
    },
}

pytest.QUOTES_MOCK = quotes_mock
