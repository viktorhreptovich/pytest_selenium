from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


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
