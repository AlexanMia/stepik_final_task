# main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице.
# Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py



from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#registration_link")
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()


        #link = self.browser.find_element_by_css_selector("#login_link")
        #link.click()
        #alert = self.browser.switch_to.alert  # Добавив обработку alert в метод go_to_login_page, мы восстановим работоспособность всех тестов, не меняя самих тестов
        #alert.accept()


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"  # Обратите внимание здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать



