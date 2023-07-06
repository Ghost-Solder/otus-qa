from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class ProductPage(BasePage):

    def load(self, product_name):
        self.base_load()
        wait = WebDriverWait(self.browser, 3, poll_frequency=1)
        wait.until(
            ec.visibility_of_element_located((By.LINK_TEXT, product_name))
        ).click()
        return self

    def check_main_objects(self, product_name):
        assert self._check_object('//h1').text == product_name
        assert self._check_object('//span[@class="price-new"]')
        assert self._check_object('//button[@type="submit"]')
        assert self._check_object('//a[@id="description-tab"]')
        assert self._check_object('//input[@name="quantity"]')
