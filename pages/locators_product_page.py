from selenium.webdriver.common.by import By


class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
