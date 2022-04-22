# файл для размещения селекторов, чтобы быстро исправить в одном месте
# locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")



class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner ")


class BasketPageLocators():
    BUTTON_BASKET_page = (By.CSS_SELECTOR, "span.btn-group")

    NOTE_ABOUT_BASKET = (By.XPATH, "//div[@id='content_inner']/p")
    #NOTE_ABOUT_BASKET = ((By.XPATH, "//p[contains(text(), 'empty')]"))
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items")





#id content_inner - надпись корзина пуста