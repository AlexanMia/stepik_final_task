from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "URL doesn't true"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration Form is not presented"

    def register_new_user(self, email, password):

        form_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        form_email.send_keys(email)


        form_passw1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        form_passw1.send_keys(password)
        form_passw2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        form_passw2.send_keys(password)
        time.sleep(10)

        registr_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        registr_button.click()


