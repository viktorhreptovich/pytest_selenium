from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        return self

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
            'Current url does not contain "login"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def register_new_user(self, email, password):
        username_input = self.browser.find_element(*LoginPageLocators.REGISTER_USERNAME_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_INPUT)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        username_input.send_keys(email)
        password_input.send_keys(password)
        password_confirm_input.send_keys(password)
        register_button.click()
