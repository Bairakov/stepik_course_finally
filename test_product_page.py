from time import time
from .pages.product_page import Product_page
from .pages.base_page import BasePage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = Product_page(browser, link)
    page.open()
    page.add_to_basket()
    #time.sleep(1000)

