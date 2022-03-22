from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID,"login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.XPATH, '//*[@id="id_registration-email"]')
    REG_PASSWORD = (By.XPATH, '//*[@id="id_registration-password1"]')
    REG_PASSWORD_CONF = (By.XPATH, '//*[@id="id_registration-password2"]')
    REG_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')

class BasketPageLocators():
    BASKET_BUTTON = (By.ID, "add_to_basket_form")
    HANDBOOK = (By.XPATH, "/html/body/div[2]/div/ul/li[5]")
    CHEAK_BOOK_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE2 = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRICE1 = (By.XPATH, "//p[@class='price_color']")
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BASKET_ITEMS = (By.XPATH, '//*[@id="basket_formset"]/div')
    BASKET_EMPTY = (By.XPATH, "//p[contains(text(), 'empty')]")



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")