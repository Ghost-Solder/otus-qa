from selenium.webdriver.common.by import By


class TestOpenCart:

    def test_main_page(self, browser):
        browser.find_element(By.XPATH, '//img[@title="Your Store"]')
        pass

    def test_catalog_page(self, browser):
        pass

    def test_product_page(self, browser):
        pass

    def test_login_to_admin_page(self, browser):
        browser.get(f'{browser.url}/admin')
        pass

    def test_registration_page(self, browser):
        browser.get(f'{browser.url}/index.php?route=account/register')
        pass
