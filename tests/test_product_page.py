import time

from pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_name = product_page.get_product_name()
    product_page.should_be_message_product_has_been_added(product_name)
    product_price = product_page.get_product_price()
    product_page.should_be_message_total_basket(product_price)
