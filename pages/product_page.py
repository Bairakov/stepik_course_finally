import time
from .base_page import BasePage
from selenium import webdriver
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class Product_page(BasePage):
    def add_to_basket_and_assert(self):
        book_text = self.browser.find_element(*BasketPageLocators.HANDBOOK).text
        price1 = self.browser.find_element(*BasketPageLocators.PRICE1).text
        BASKET = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        BASKET.click()
        
        alert = self.solve_quiz_and_get_code()
        self.browser.implicitly_wait(10)
        
        book_text2 = self.browser.find_element(*BasketPageLocators.CHEAK_BOOK_IN_BASKET).text
        price2 = self.browser.find_element(*BasketPageLocators.PRICE2).text
        assert book_text == book_text2, "Название книг не совпадают"
        assert price1 == price2, "Цены не совпадают"
        print(book_text2)
        print(price2)
        


    def add_to_basket(self):
        BASKET = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        BASKET.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be" 
                
    def wait_until_the_element_disappears(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"