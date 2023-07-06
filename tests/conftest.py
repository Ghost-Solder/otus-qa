import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions

from pages.admin_page import AdminPage
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Browser name (firefox, chrome, safari, edge, yandex)')
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


@pytest.fixture(scope='module')
def main_page(browser: 'webdriver') -> 'MainPage':
    return MainPage(browser)


@pytest.fixture(scope='module')
def admin_page(browser: 'webdriver') -> 'AdminPage':
    return AdminPage(browser)


@pytest.fixture(scope='module')
def catalog_page(browser: 'webdriver') -> 'CatalogPage':
    return CatalogPage(browser)


@pytest.fixture(scope='module')
def product_page(browser: 'webdriver') -> 'ProductPage':
    return ProductPage(browser)


@pytest.fixture(scope='module')
def registration_page(browser: 'webdriver') -> 'RegistrationPage':
    return RegistrationPage(browser)
