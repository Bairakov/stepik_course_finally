from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        pass