# Регистрация нового пользователя в магазине опенкарта.
from typing_extensions import Self

from pages.base_page import BasePage


class RegistrationPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.url = browser.url + '/index.php?route=account/register'

    def check_main_objects(self) -> Self:
        assert self._find_object('//h1').text == 'Register Account'
        assert self._find_object('//input[@name="firstname"]')
        assert self._find_object('//input[@name="lastname"]')
        assert self._find_object('//input[@name="email"]')
        assert self._find_object('//button[@type="submit"]')
        return self
