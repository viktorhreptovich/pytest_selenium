import pytest

from pages.product_page import ProductPage


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param(
#                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#                                       "?promo=offer7",
#                                       marks=pytest.mark.xfail
#                                   ),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_go_to_login_page(browser, link):
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_add_to_basket_button()
#     product_page.add_to_basket()
#     product_page.solve_quiz_and_get_code()
#     product_name = product_page.get_product_name()
#     product_page.should_be_message_product_has_been_added(product_name)
#     product_price = product_page.get_product_price()
#     product_page.should_be_message_total_basket(product_price)

@pytest.mark.xfail(reason="example fail negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_message_product_has_been_added()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_message_product_has_been_added()


@pytest.mark.xfail(reason="example fail negative test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappeared_message_product_has_been_added()
