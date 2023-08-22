import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing_extensions import Self

from pages.base_page import BasePage


class AdminPage(BasePage):
    CREDS = {'login': 'demo', 'password': 'demo'}

    INPUT_USERNAME = '//input[@name="username"]'
    INPUT_PASSWORD = '//input[@name="password"]'
    BTN_SUBMIT = '//button[@type="submit"]'
    BTN_MODAL_CLOSE = '//button[@class="btn-close"]'
    HREF_CATALOG = '//a[@href="#collapse-1"]'

    def __init__(self, browser: 'webdriver'):
        super().__init__(browser)
        self.url = browser.url + '/admin'

    @allure.step('Check main objects for the admin page')
    def check_main_objects(self) -> Self:
        assert self._find_object(
            '//div[@class="card-header"]').text == 'Please enter your login details.'
        assert self._find_object(self.INPUT_USERNAME)
        assert self._find_object(self.INPUT_PASSWORD)
        assert self._find_object(self.BTN_SUBMIT)
        assert self._find_object('//div[@class="mb-3"]').text == 'Forgotten Password'
        return self

    @allure.step('Fill login and password on the admin page - {login} / {password}')
    def fill_login_page(self, login: str, password: str) -> Self:
        self._find_object(self.INPUT_USERNAME).send_keys(login)
        self._find_object(self.INPUT_PASSWORD).send_keys(password)
        return self

    @allure.step('Login to admin')
    def login_to_admin(self) -> Self:
        self.fill_login_page(**self.CREDS)
        self._find_object(self.BTN_SUBMIT).click()
        return self

    @allure.step('Close modal window after login to admin')
    def close_modal(self) -> Self:
        self._find_object(self.BTN_MODAL_CLOSE).click()
        return self

    @allure.step('Open catalog on the admin page')
    def open_catalog(self) -> Self:
        self._find_object(self.HREF_CATALOG).click()
        self.browser.find_element(By.LINK_TEXT, 'Products').click()
        return self

    @allure.step('Start adding new product')
    def add_new_product(self) -> Self:
        self.open_catalog()
        self._find_object('//a[@area-label="Add New"]').click()
        self._find_object('//input[@id="input-name-1"]').send_keys('something_new')
        self._find_object('//input[@id="input-meta-title-1"]').send_keys('something_new')
        self._find_object('//a[@area-label="Save"]').click()
        return self

    @allure.step('Delete product')
    def delete_product(self) -> Self:
        self.open_catalog()
        self._find_object('//input[@value="40"]').click()
        self._find_object('//a[@area-label="Delete"]').click()
        self.browser.swithTo().alert().accept()
        return self
