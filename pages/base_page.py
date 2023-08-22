from typing import Any

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from typing_extensions import Self


class BasePage:

    def __init__(self, browser: 'webdriver'):
        self.browser = browser
        self.url = browser.url

    @allure.step('Load page')
    def base_load(self) -> Self:
        allure.attach(self.url)
        self.browser.get(self.url)
        return self

    @allure.step('Find object using xpath - {xpath}')
    def _find_object(self, xpath: str) -> Any:
        wait = WebDriverWait(self.browser, 10, poll_frequency=1)
        return wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
