from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pages.admin_page import AdminPage
    from pages.catalog_page import CatalogPage
    from pages.main_page import MainPage
    from pages.product_page import ProductPage
    from pages.registration_page import RegistrationPage


class TestOpenCart:

    def test_main_page(self, main_page: 'MainPage'):
        main_page.base_load().check_main_objects()

    @pytest.mark.parametrize('currency', ['EUR', 'GBP', 'USD'])
    def test_switch_currency(self, main_page: 'MainPage', currency: str):
        main_page.base_load().switch_currency(currency)

    def test_catalog_page(self, catalog_page: 'CatalogPage'):
        catalog_page.load().check_main_objects()

    @pytest.mark.parametrize('product_name', [
        'MacBook',
        'iPhone',
        'Apple Cinema 30"',
        'Canon EOS 5D',
    ])
    def test_product_page(self, product_page: 'ProductPage', product_name: str):
        product_page.load(product_name).check_main_objects(product_name)

    def test_login_form_of_admin_page(self, admin_page: 'AdminPage'):
        admin_page.base_load().check_main_objects()

    def test_add_product(self, login_to_admin_page: 'AdminPage', admin_page: 'AdminPage'):
        admin_page.close_modal().add_new_product()

    def test_delete_product(self, login_to_admin_page: 'AdminPage', admin_page: 'AdminPage'):
        admin_page.close_modal().delete_product()

    def test_registration_page(self, registration_page: 'RegistrationPage'):
        registration_page.base_load().check_main_objects()

    def test_registration_new_user(self, registration_page: 'RegistrationPage'):
        registration_page.base_load()
        registration_page.fill_registration_form_with_fake_data()
        registration_page.registrate_user()
