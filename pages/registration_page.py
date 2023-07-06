# Регистрация нового пользователя в магазине опенкарта.

from pages.base_page import BasePage


class RegistrationPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.url = browser.url + '/index.php?route=account/register'

    def check_main_objects(self):
        assert self._check_object('//h1').text == 'Register Account'
        assert self._check_object('//input[@name="firstname"]')
        assert self._check_object('//input[@name="lastname"]')
        assert self._check_object('//input[@name="email"]')
        assert self._check_object('//button[@type="submit"]')
