import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        default='https://ya.ru',
        help='url for status checking',
    )

    parser.addoption(
        '--status_code',
        default=200,
        help='expected status code',
    )


@pytest.fixture
def base_url(request) -> str:
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request) -> int:
    return request.config.getoption('--status_code')
