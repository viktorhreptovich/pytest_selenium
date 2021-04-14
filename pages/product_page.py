import re

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_product_url(self):
        assert 'catalogue' in self.browser.current_url, \
            'Current url does not contain "catalogue"'

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            '"Add to basket" button is not presented'

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def should_be_message_product_has_been_added(self, product_name):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_HAS_BEEN_ADDED), \
            'Message "Product has been added to basket" is not presented'
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_HAS_BEEN_ADDED).text
        assert product_name in message, \
            f'Message "{message}" doesn\'t contain product name "{product_name}"'

    def should_be_message_total_basket(self, product_price):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), \
            'Message "Basket total" is not presented'
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        assert product_price in message, \
            f'Message "{message}" doesn\'t contain product name "{product_price}"'
