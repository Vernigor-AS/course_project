import time

import pytest
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage



@pytest.mark.registration_new_user
class TestUserAddToBasketFromProductPage():
    #фикстура регистрации нового пользователя
    @pytest.fixture(scope="function", autouse=True)
    def setup_new_user(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page_registration = LoginPage(browser, link)
        page_registration.open()
        page_registration.registration_new_user()
        page_registration.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_add_product_to_cart()
        product_page.check_product_name_add_to_cart()
        product_page.check_price_product()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-"
                                               "work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser,link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_product_to_cart()
    result = BasePage(browser, link)
    result.solve_quiz_and_get_code()
    product_page.check_product_name_add_to_cart()
    product_page.check_price_product()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_product_to_cart()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_product_to_cart()
    product_page.is_element_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    basket_page_link = 'http://selenium1py.pythonanywhere.com/ru/basket/'
    guest = ProductPage(browser, link)
    guest.open()
    guest.guest_open_cart()
    basket = BasketPage(browser, basket_page_link)
    basket.check_that_there_are_no_items_in_the_cart()
    basket.check_the_message_about_the_empty_cart()

