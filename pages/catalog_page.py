from typing_extensions import Self

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class CatalogPage(BasePage):

    def load(self) -> Self:
        self.base_load()
        self.browser.find_element(By.LINK_TEXT, 'Desktops').click()
        wait = WebDriverWait(self.browser, 3, poll_frequency=1)
        all_desktops = wait.until(
            ec.visibility_of_element_located((By.LINK_TEXT, 'Show All Desktops'))
        )
        all_desktops.click()
        return self

    def check_main_objects(self) -> Self:
        assert self._find_object('//a[@title="Checkout"]')
        assert self._find_object('//div[@id="content"]/h2').text == 'Desktops'
        assert self._find_object('//a[@id="compare-total"]')
        assert self._find_object('//select[@id="input-sort"]')
        assert self._find_object('//select[@id="input-limit"]')
        return self
