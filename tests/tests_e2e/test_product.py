from http import HTTPStatus

from cerberus import Validator

from tests.schemas.contract_product import contract_product

PATH_API_PRODUCT = "/v1/products/"


def test_api_product(client, response_mock_quotes):
    request = client.get(PATH_API_PRODUCT)

    if request.status_code != HTTPStatus.OK:
        raise
    validator_schema = Validator()
    response_is_valid = validator_schema.validate(request.json(), contract_product)

    if not response_is_valid:
        raise Exception(str(validator_schema.errors))

    assert response_is_valid == True
