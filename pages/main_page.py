import allure
from typing_extensions import Self

from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Check main objects on the main page')
    def check_main_objects(self) -> Self:
        assert self._find_object('//img[@title="Your Store"]')
        assert self._find_object('//img[@alt="iPhone 6"]')
        assert self._find_object('//input[@name="search"]')
        assert self._find_object('//button/i[@class="fas fa-shopping-cart"]')
        assert self._find_object('//a[@title="Checkout"]')
        return self

    @allure.step('Switch currency to {currency}')
    def switch_currency(self, currency: str) -> Self:
        self._find_object('//form[@id="form-currency"]').click()
        self._find_object(f'//a[@href="{currency}"]').click()
        main_currency = self._find_object('//a[@href="#"]/strong').text
        price_currency = self._find_object('//span[@class="price-new"]')
        price_currency = price_currency.text[-1] if currency is 'EUR' else price_currency.text[0]
        assert main_currency == price_currency
        return self
