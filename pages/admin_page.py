# Добавление нового товара в разделе администратора.
# Удаление товара из списка в разделе администартора.

from pages.base_page import BasePage


class AdminPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.url = browser.url + '/admin'

    def check_main_objects(self):
        assert self._find_object(
            '//div[@class="card-header"]').text == 'Please enter your login details.'
        assert self._find_object('//input[@name="username"]')
        assert self._find_object('//input[@name="password"]')
        assert self._find_object('//button[@type="submit"]')
        assert self._find_object('//div[@class="mb-3"]').text == 'Forgotten Password'
