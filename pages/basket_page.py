import time
from .base_page import BasePage
from selenium import webdriver
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class Basket_page(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "the products are in the basket, but should not be"

    def should_be_text_basket_is_empty(self):
         assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "there is no text that the basket is empty"