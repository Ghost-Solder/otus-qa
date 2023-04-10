import requests


def test_statuses(base_url, status_code):
    response = requests.get(url=base_url)
    assert response.status_code == int(status_code)
