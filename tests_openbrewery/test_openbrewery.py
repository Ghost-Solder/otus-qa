from typing import TYPE_CHECKING

import pytest
import requests

from jsonschema import validate

if TYPE_CHECKING:
    from requests import Response


def validate_response(response: 'Response', schema: dict) -> None:
    assert response.status_code == 200
    assert validate(instance=response.json(), schema=schema) is None


class TestsOpenBreweryApi:
    """Some positive tests for Open Brewery Api https://www.openbrewerydb.org/documentation"""

    brewery_api_url = 'https://api.openbrewerydb.org/v1/breweries'

    brewery_schema = {
        'type': 'array',
        'items': {
            'type': 'object',
            'properties': {
                'id': {'type': ['null', 'string']},
                'name': {'type': 'string'},
                'brewery_type': {'type': 'string'},
                'address_1': {'type': ['null', 'string']},
                'address_2': {'type': ['null', 'string']},
                'address_3': {'type': ['null', 'string']},
                'city': {'type': 'string'},
                'state_province': {'type': 'string'},
                'postal_code': {'type': 'string'},
                'country': {'type': 'string'},
                'longitude': {'type': ['null', 'string']},
                'latitude': {'type': ['null', 'string']},
                'phone': {'type': ['null', 'string']},
                'website_url': {'type': ['null', 'string']},
                'state': {'type': 'string'},
                'street': {'type': ['null', 'string']},
            },
        },
    }

    @pytest.mark.parametrize('number', [1, 3, 20])
    def test_breweries_list(self, number: int):
        payload = {'per_page': number}
        response = requests.get(self.brewery_api_url, params=payload)
        validate_response(response, self.brewery_schema)

    @pytest.mark.parametrize('state', ['California', 'New York'])
    def test_get_breweries_by_state(self, state: str):
        payload = {'by_state': state}
        response = requests.get(self.brewery_api_url, params=payload)
        validate_response(response, self.brewery_schema)

    @pytest.mark.parametrize('city', ['San Francisco', 'Los Angeles'])
    def test_get_breweries_by_city(self, city: str):
        payload = {'by_state': city}
        response = requests.get(self.brewery_api_url, params=payload)
        validate_response(response, self.brewery_schema)

    @pytest.mark.parametrize('brewery_type', ['micro', 'nano'])
    def test_get_breweries_by_type(self, brewery_type: str):
        payload = {'by_state': brewery_type}
        response = requests.get(self.brewery_api_url, params=payload)
        validate_response(response, self.brewery_schema)

    @pytest.mark.parametrize('postal_code', ['94102', '10001'])
    def test_get_breweries_by_postal_code(self, postal_code: str):
        payload = {'by_state': postal_code}
        response = requests.get(self.brewery_api_url, params=payload)
        validate_response(response, self.brewery_schema)
