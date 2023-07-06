from typing_extensions import Self

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class ProductPage(BasePage):

    def load(self, product_name: str) -> Self:
        self.base_load()
        wait = WebDriverWait(self.browser, 3, poll_frequency=1)
        wait.until(
            ec.visibility_of_element_located((By.LINK_TEXT, product_name))
        ).click()
        return self

    def check_main_objects(self, product_name: str) -> Self:
        assert self._find_object('//h1').text == product_name
        assert self._find_object('//span[@class="price-new"]')
        assert self._find_object('//button[@type="submit"]')
        assert self._find_object('//a[@id="description-tab"]')
        assert self._find_object('//input[@name="quantity"]')
        return self
