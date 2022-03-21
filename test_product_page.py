from time import time
from .pages.product_page import Product_page
from .pages.base_page import BasePage
import time
import pytest


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
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{link}"
    page = Product_page(browser, link)
    page.open()
    page.add_to_basket()
    #time.sleep(1000)


