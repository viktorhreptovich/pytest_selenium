from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_have_products(self):
        products = self.browser.find_elements(*BasketPageLocators.PRODUCT_ITEMS)
        assert len(products) == 0, \
            f'Basket isn\'t empty, products count = {len(products)}'

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            'Message "Empty basket" is presented'
