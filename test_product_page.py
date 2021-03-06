import email
from os import link
from time import time
from .pages.product_page import Product_page
from .pages.base_page import BasePage
import time
import pytest
from .pages.basket_page import Basket_page
from .pages.login_page import LoginPage
import functools
import random


@pytest.mark.parametrize('link', ["promo=offer0",
                                 "promo=offer1",
                                  "promo=offer2",
                                  "promo=offer3",
                                  "promo=offer4",
                                  "promo=offer5",
                                  "promo=offer6",
                                  pytest.param("promo=offer7", marks=pytest.mark.xfail),
                                  "promo=offer8",
                                  "promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = Product_page(browser, link)
    page.open()
    page.add_to_basket_and_assert()
    
    

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = Product_page(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = Product_page(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = Product_page(browser, link)
    page.open()
    page.add_to_basket()
    page.wait_until_the_element_disappears()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Product_page(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Product_page(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = Basket_page(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_products_in_basket()
    page.should_be_text_basket_is_empty()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    page = Basket_page(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_products_in_basket()
    page.should_be_text_basket_is_empty()

@pytest.mark.reg_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        a = functools.partial(random.randint, 0, 9)
        email = lambda: "test1{}{}{}@gmail.ru".format(a(), a(), a(), a(), a(), a())
        email = str(email())
        password = "128mb2312ksdfg"
        page.register_new_user(email, password)
        time.sleep(5)
        page.should_be_authorized_user()
        
        

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = Product_page(browser, link)
        page.open()
        page.should_not_be_success_message()


    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = Product_page(browser, link)
        page.open()
        page.add_to_basket_and_assert()