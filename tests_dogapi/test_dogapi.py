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


class TestsDogApi:
    """Some positive tests for Dogs Api https://dog.ceo/dog-api/documentation/"""

    dogapi_url = 'https://dog.ceo/api'

    schema = {
        'type': 'object',
        'properties': {
            'message': {'type': ['object', 'string', 'array']},
            'status': {'type': 'string'},
        },
        'required': ['message', 'status'],
    }

    def test_breeds_list(self):
        response = requests.get(f'{self.dogapi_url}/breeds/list/all')
        validate_response(response, self.schema)

    def test_single_random_image(self):
        response = requests.get(f'{self.dogapi_url}/breeds/image/random')
        validate_response(response, self.schema)

    @pytest.mark.parametrize('number', [1, 20, 50])
    def test_multiple_random_images(self, number: int):
        response = requests.get(f'{self.dogapi_url}/breeds/image/random/{number}')
        validate_response(response, self.schema, number)

    @pytest.mark.parametrize('breed', [
        'affenpinscher',
    ])
    def test_all_images_by_breed(self, breed: str):
        response = requests.get(f'{self.dogapi_url}/breed/{breed}/images')
        validate_response(response, self.schema)

    @pytest.mark.parametrize('number', [1, 20, 50])
    @pytest.mark.parametrize('breed', [
        'affenpinscher',
    ])
    def test_images_by_breed(self, number: int, breed: str):
        url = f'{self.dogapi_url}/breed/{breed}/images/random'
        response = requests.get(f'{url}/{number}')
        validate_response(response, self.schema, number)

    @pytest.mark.parametrize('breed', [
        'affenpinscher',
    ])
    def test_subbreed_list(self, breed: str):
        response = requests.get(f'{self.dogapi_url}/breed/{breed}/list')
        validate_response(response, self.schema)

    @pytest.mark.parametrize('breed, subbreed', [
        ('hound', 'afghan'),
    ])
    def test_all_images_by_subbreed(self, breed: str, subbreed: str):
        response = requests.get(f'{self.dogapi_url}/breed/{breed}/{subbreed}/images')
        validate_response(response, self.schema)

    @pytest.mark.parametrize('number', [1, 20, 50])
    @pytest.mark.parametrize('breed, subbreed', [
        ('hound', 'afghan'),
    ])
    def test_multiple_images_by_subbreed(self, breed: str, subbreed: str, number: int):
        url = f'{self.dogapi_url}/breed/{breed}/{subbreed}/images/random'
        response = requests.get(f'{url}/{number}')
        validate_response(response, self.schema, number)
