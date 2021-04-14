from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/')
    main_page.open()
    login_page = main_page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    main_page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/')
    main_page.open()
    main_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/')
    main_page.open()
    basket_page = main_page.go_to_basket_page()
    basket_page.should_not_have_products()
    basket_page.should_be_message_empty_basket()
