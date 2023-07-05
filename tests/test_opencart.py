from typing import TYPE_CHECKING, Any

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


if TYPE_CHECKING:
    from selenium import webdriver


def check_object(browser: 'webdriver', xpath: str) -> Any:
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    return wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))


class TestOpenCart:

    def test_main_page(self, browser: 'webdriver'):
        browser.get(browser.url)
        assert check_object(browser, '//img[@title="Your Store"]')
        assert check_object(browser, '//img[@alt="iPhone 6"]')
        assert check_object(browser, '//input[@name="search"]')
        assert check_object(browser, '//button/i[@class="fas fa-shopping-cart"]')
        assert check_object(browser, '//a[@title="Checkout"]')

    def test_catalog_page(self, browser: 'webdriver'):
        browser.get(browser.url)
        browser.find_element(By.LINK_TEXT, 'Desktops').click()
        wait = WebDriverWait(browser, 3, poll_frequency=1)
        all_desktops = wait.until(
            ec.visibility_of_element_located((By.LINK_TEXT, 'Show All Desktops'))
        )
        all_desktops.click()
        assert check_object(browser, '//a[@title="Checkout"]')
        assert check_object(browser, '//div[@id="content"]/h2').text == 'Desktops'
        assert check_object(browser, '//a[@id="compare-total"]')
        assert check_object(browser, '//select[@id="input-sort"]')
        assert check_object(browser, '//select[@id="input-limit"]')

    def test_product_page(self, browser: 'webdriver'):
        browser.get(browser.url)
        wait = WebDriverWait(browser, 3, poll_frequency=1)
        wait.until(
            ec.visibility_of_element_located((By.LINK_TEXT, 'MacBook'))
        ).click()
        assert check_object(browser, '//h1').text == 'MacBook'
        assert check_object(browser, '//span[@class="price-new"]')
        assert check_object(browser, '//button[@type="submit"]')
        assert check_object(browser, '//a[@id="description-tab"]')
        assert check_object(browser, '//input[@name="quantity"]')

    def test_login_to_admin_page(self, browser: 'webdriver'):
        browser.get(f'{browser.url}/admin')
        assert check_object(
            browser, '//div[@class="card-header"]').text == 'Please enter your login details.'
        assert check_object(browser, '//input[@name="username"]')
        assert check_object(browser, '//input[@name="password"]')
        assert check_object(browser, '//button[@type="submit"]')
        assert check_object(browser, '//div[@class="mb-3"]').text == 'Forgotten Password'

    def test_registration_page(self, browser: 'webdriver'):
        browser.get(f'{browser.url}/index.php?route=account/register')
        assert check_object(browser, '//h1').text == 'Register Account'
        assert check_object(browser, '//input[@name="firstname"]')
        assert check_object(browser, '//input[@name="lastname"]')
        assert check_object(browser, '//input[@name="email"]')
        assert check_object(browser, '//button[@type="submit"]')
