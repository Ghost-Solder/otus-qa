import allure
from faker import Faker
from selenium import webdriver
from typing_extensions import Self

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    INPUT_FIRST_NAME = '//input[@name="firstname"]'
    INPUT_LAST_NAME = '//input[@name="lastname"]'
    INPUT_EMAIL = '//input[@name="email"]'
    INPUT_PASSWORD = '//input[@name="password"]'
    CHECKBOX_POLICY = '//input[@name="agree"]'
    BTN_SUBMIT = '//button[@type="submit"]'

    def __init__(self, browser: 'webdriver'):
        super().__init__(browser)
        self.url = browser.url + '/index.php?route=account/register'

    @allure.step('Check main objects on the registration page')
    def check_main_objects(self) -> Self:
        assert self._find_object('//h1').text == 'Register Account'
        assert self._find_object(self.INPUT_FIRST_NAME)
        assert self._find_object(self.INPUT_LAST_NAME)
        assert self._find_object(self.INPUT_EMAIL)
        assert self._find_object(self.INPUT_PASSWORD)
        assert self._find_object(self.BTN_SUBMIT)
        return self

    @allure.step('Fill registration form - {firstname}, {lastname}, {email}, {password}')
    def fill_registration_form(
        self,
        firstname: str,
        lastname: str,
        email: str,
        password: str,
    ) -> Self:
        self._find_object(self.INPUT_FIRST_NAME).send_keys(firstname)
        self._find_object(self.INPUT_LAST_NAME).send_keys(lastname)
        self._find_object(self.INPUT_EMAIL).send_keys(email)
        self._find_object(self.INPUT_PASSWORD).send_keys(password)
        self._find_object(self.CHECKBOX_POLICY).click()
        return self

    @allure.step('Fill registration form with fake data')
    def fill_registration_form_with_fake_data(self) -> Self:
        fake = Faker()
        full_name = fake.name()
        firstname = full_name.split()[0]
        lastname = full_name.split()[1]
        email = fake.email()
        password = fake.password(length=4)
        user = {'firstname': firstname, 'lastname': lastname, 'email': email, 'password': password}
        allure.attach(user)
        self.fill_registration_form(**user)
        return self

    @allure.step('Registrate user')
    def registrate_user(self) -> Self:
        self._find_object(self.BTN_SUBMIT).click()
        assert self._find_object('//h1').text == 'Your Account Has Been Created!'
        return self
