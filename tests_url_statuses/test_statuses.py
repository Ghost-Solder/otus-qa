import requests


def test_statuses(base_url: str, status_code: int):
    response = requests.get(url=base_url)
    assert response.status_code == int(status_code)
