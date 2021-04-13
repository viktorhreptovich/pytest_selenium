from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/')
    main_page.open()
    login_page = main_page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/')
    page.open()
    page.should_be_login_link()
