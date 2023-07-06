from typing import Any

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from typing_extensions import Self


class BasePage:

    def __init__(self, browser: 'webdriver'):
        self.browser = browser
        self.url = browser.url

    def base_load(self) -> Self:
        self.browser.get(self.url)
        return self

    def _find_object(self, xpath: str) -> Any:
        wait = WebDriverWait(self.browser, 10, poll_frequency=1)
        return wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
