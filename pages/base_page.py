import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser  # type: WebDriver
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, value):
        try:
            self.browser.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    def is_not_element_present(self, by, value, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located((by, value))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                expected_conditions.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        from pages.login_page import LoginPage
        return LoginPage(self.browser, self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_button.click()
        from pages.basket_page import BasketPage
        return BasketPage(self.browser, self.browser.current_url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"
