import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Browser name (firefox, chrome, opera, safari, edge, yandex)')
    parser.addoption('--url', action='store', default='https://demo.opencart.com/',
                     help='Base URL for the tests')


@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')

    match browser:
        case 'firefox':
            options = FirefoxOptions()
            driver = webdriver.Firefox(options=options)
        case 'chrome':
            options = ChromeOptions()
            driver = webdriver.Chrome(options=options)
        case 'safari':
            options = SafariOptions()
            driver = webdriver.Safari(options=options)
        case 'edge':
            options = EdgeOptions()
            driver = webdriver.Edge(options=options)
        case 'yandex':
            options = ChromeOptions()
            options.binary_location = '/path/to/yandex/browser'
            driver = webdriver.Chrome(options=options)
        case _:
            raise ValueError(f'Invalid browser: {browser}')

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
