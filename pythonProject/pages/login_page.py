from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    #регистрация нового пользователя
    def registration_new_user(self):
        user_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_NEW_USER_EMAIL)
        user_email.send_keys(str(time.time()) + "@fakemail.org")
        user_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_NEW_USER_PASSWORD)
        user_password.send_keys('balalaika100')
        user_confirm_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_NEW_USER_CONFIRM_PASSWORD)
        user_confirm_password.send_keys('balalaika100')
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        submit_button.click()



    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, f"Expected 'login' to be in URL, but got {current_url}"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'


    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Registration form is not presented'