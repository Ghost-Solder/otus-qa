import pytest


class TestOpenCart:

    def test_main_page(self, main_page):
        main_page.base_load().check_main_objects()

    def test_catalog_page(self, catalog_page):
        catalog_page.load().check_main_objects()

    @pytest.mark.parametrize('product_name', [
        'MacBook',
        'iPhone',
        'Apple Cinema 30"',
        'Canon EOS 5D',
    ])
    def test_product_page(self, product_page, product_name):
        product_page.load(product_name).check_main_objects(product_name)

    def test_login_to_admin_page(self, admin_page):
        admin_page.base_load().check_main_objects()

    def test_registration_page(self, registration_page):
        registration_page.base_load().check_main_objects()
