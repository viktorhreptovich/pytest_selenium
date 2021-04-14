from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.header a.btn')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button.btn-add-to-basket')
    MESSAGE_PRODUCT_HAS_BEEN_ADDED = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner')
    MESSAGE_PRODUCT_HAS_BEEN_ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner strong')
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) .alertinner')
    MESSAGE_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) .alertinner strong')


class BasketPageLocators:
    PRODUCT_ITEMS = (By.CSS_SELECTOR, '#basket_formset .basket-items')
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner>p')
