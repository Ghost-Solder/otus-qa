# Переключение валют из верхнего меню опенкарта.

from pages.base_page import BasePage


class MainPage(BasePage):

    def check_main_objects(self):
        assert self._check_object('//img[@title="Your Store"]')
        assert self._check_object('//img[@alt="iPhone 6"]')
        assert self._check_object('//input[@name="search"]')
        assert self._check_object('//button/i[@class="fas fa-shopping-cart"]')
        assert self._check_object('//a[@title="Checkout"]')
