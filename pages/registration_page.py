# Регистрация нового пользователя в магазине опенкарта.
from selenium import webdriver
from typing_extensions import Self

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    INPUT_FIRST_NAME = '//input[@name="firstname"]'
    INPUT_LAST_NAME = '//input[@name="lastname"]'
    INPUT_EMAIL = '//input[@name="email"]'
    BTN_SUBMIT = '//button[@type="submit"]'

    def __init__(self, browser: 'webdriver'):
        super().__init__(browser)
        self.url = browser.url + '/index.php?route=account/register'

    def check_main_objects(self) -> Self:
        assert self._find_object('//h1').text == 'Register Account'
        assert self._find_object(self.INPUT_FIRST_NAME)
        assert self._find_object(self.INPUT_LAST_NAME)
        assert self._find_object(self.INPUT_EMAIL)
        assert self._find_object(self.BTN_SUBMIT)
        return self
