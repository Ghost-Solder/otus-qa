from typing import TYPE_CHECKING, Optional

import pytest
import requests

from jsonschema import validate

if TYPE_CHECKING:
    from requests import Response


def validate_response(response: 'Response', schema: dict, number: Optional[int] = None) -> None:
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)
    if number is not None:
        assert len(response.json()['message']) == number


class TestsOpenBreweryApi:
    """Some positive tests for Open Brewery Api https://www.openbrewerydb.org/documentation"""

    openbrewery_api_url = 'https://api.openbrewerydb.org/v1/breweries'

    schema = {
        'type': 'array',
        'items': {
            'type': 'object',
            'properties': {
                "id": {'type': 'string'},
                "name": {'type': 'string'},
                "brewery_type": {'type': 'string'},
                "address_1": {'type': ['null', 'string']},
                "address_2": {'type': ['null', 'string']},
                "address_3": {'type': ['null', 'string']},
                "city": {'type': 'string'},
                "state_province": {'type': 'string'},
                "postal_code": {'type': 'string'},
                "country": {'type': 'string'},
                "longitude": {'type': ['null', 'string']},
                "latitude": {'type': ['null', 'string']},
                "phone": {'type': 'string'},
                "website_url": {'type': ['null', 'string']},
                "state": {'type': 'string'},
                "street": {'type': 'string'},
            },
        },
    }

    @pytest.mark.parametrize('number', [1, 3, 20])
    def test_breweries_list(self, number: int):
        payload = {'per_page': number}
        response = requests.get(f'{self.openbrewery_api_url}', params=payload)
        validate_response(response, self.schema)
