import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time

#tests in стиле Page Object
# test_main_page.py - тут мы выполняем сами тесты
# Здесь мы будем создавать функции, которым:
# выдаём нужный для проверки линк
# созаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага №1
# следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
# добавляем проверки, которые создавали методами в main_page.py


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        # link = " http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        # link = " http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()




@pytest.mark.smoke
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    time.sleep(5)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_things_in_basket()
    basket_page.should_be_note_about_empty_basket()







    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    #page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    #page.open()  # открываем страницу
    #page.go_to_add_basket()
    #page.go_to_basket_page()
    #time.sleep(5)

    #basket_page = BasketPage(browser, browser.current_url)

    #basket_page.should_not_be_things_in_basket()
    #time.sleep(15)
    #basket_page.should_be_note_about_empty_basket()