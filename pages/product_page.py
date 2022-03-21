import time
from .base_page import BasePage
from selenium import webdriver
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class Product_page(BasePage):
    def add_to_basket(self):
        book_text = self.browser.find_element(*BasketPageLocators.HANDBOOK).text
        price1 = self.browser.find_element(*BasketPageLocators.PRICE1).text
        BASKET = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        BASKET.click()
        
        alert = self.solve_quiz_and_get_code()
        time.sleep(5)
        
        book_text2 = self.browser.find_element(*BasketPageLocators.CHEAK_BOOK_IN_BASKET).text
        price2 = self.browser.find_element(*BasketPageLocators.PRICE2).text
        assert book_text == book_text2, "Название книг не совпадают"
        assert price1 == price2, "Цены не совпадают"
        print(book_text2)
        print(price2)
        


