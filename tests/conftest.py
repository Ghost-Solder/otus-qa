import os

import allure
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
    parser.addoption('--browser', action='store', default='edge',
                     help='Browser name (firefox, chrome, safari, edge, yandex)')
    parser.addoption('--url', action='store', default='https://demo.opencart.com/',
                     help='Base URL for the tests')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')

    match browser:
        case 'firefox':
            options = FirefoxOptions()
            options.add_argument("--headless")
            options.add_argument('--no-sandbox')
            driver = webdriver.Firefox(options=options)
        case 'chrome':
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(options=options)
        case 'safari':
            options = SafariOptions()
            driver = webdriver.Safari(options=options)
        case 'edge':
            options = EdgeOptions()
            driver = webdriver.Edge(options=options)
        case 'yandex':
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument('--no-sandbox')
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
def login_to_admin_page(admin_page: 'AdminPage') -> 'AdminPage':
    return admin_page.base_load().login_to_admin()


@pytest.fixture(scope='module')
def catalog_page(browser: 'webdriver') -> 'CatalogPage':
    return CatalogPage(browser)


@pytest.fixture(scope='module')
def product_page(browser: 'webdriver') -> 'ProductPage':
    return ProductPage(browser)


@pytest.fixture(scope='module')
def registration_page(browser: 'webdriver') -> 'RegistrationPage':
    return RegistrationPage(browser)
