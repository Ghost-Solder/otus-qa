import http
import json
from typing import TYPE_CHECKING, Optional

import pytest
import requests

from jsonschema import validate

if TYPE_CHECKING:
    from requests import Response


def validate_response(response: 'Response', expected_status: int, schema: dict) -> None:
    assert response.status_code == expected_status
    assert validate(instance=json.loads(response.text), schema=schema) is None


class TestsJsonPlaceholderApi:
    """Some positive tests for Json Placeholder Api https://jsonplaceholder.typicode.com/guide/"""

    SUCCESS = http.HTTPStatus.OK
    CREATED = http.HTTPStatus.CREATED

    jsonplaceholder_api_url = 'https://jsonplaceholder.typicode.com/todos'

    response_schema = {
        'type': ['object', 'array'],
        'items': {
            'type': 'object',
            'properties': {
                'userId': {'type': 'number'},
                'id': {'type': 'number'},
                'title': {'type': 'string'},
                'completed': {'type': 'boolean'}
            },
            'required': ['userId', 'id', 'title', 'completed']
        }
    }

    def test_get_all_todos(self):
        response = requests.get(self.jsonplaceholder_api_url)
        validate_response(response, self.SUCCESS, self.response_schema)

    @pytest.mark.parametrize('todo_id', [1, 2, 3])
    def test_get_todo_by_id(self, todo_id):
        response = requests.get(f'{self.jsonplaceholder_api_url}/{todo_id}')
        validate_response(response, self.SUCCESS, self.response_schema)

    def test_create_todo(self):
        todo_data = {
            'userId': 1,
            'title': 'New Todo',
            'completed': False
        }
        response = requests.post(self.jsonplaceholder_api_url, json=todo_data)
        validate_response(response, self.CREATED, self.response_schema)

    @pytest.mark.parametrize('todo_id', [1, 2, 3])
    def test_update_todo(self, todo_id):
        todo_data = {
            'id': todo_id,
            'userId': 1,
            'title': 'Updated Todo',
            'completed': True
        }
        response = requests.put(f'{self.jsonplaceholder_api_url}/{todo_id}', json=todo_data)
        validate_response(response, self.SUCCESS, self.response_schema)

    @pytest.mark.parametrize('todo_id', [1, 2, 3])
    def test_delete_todo(self, todo_id):
        response = requests.delete(f'{self.jsonplaceholder_api_url}/{todo_id}')
        assert response.status_code == 200
