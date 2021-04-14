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
        product_name_in_message = self.browser.find_element(
            *ProductPageLocators.MESSAGE_PRODUCT_HAS_BEEN_ADDED_PRODUCT_NAME).text
        assert product_name_in_message == product_name, f'Expected: {product_name}, actual: {product_name_in_message}'

    def should_be_message_total_basket(self, product_price):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), \
            'Message "Basket total" is not presented'
        price_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL_PRICE).text
        assert price_in_message == product_price, f'Expected: {product_price}, actual: {price_in_message}'
