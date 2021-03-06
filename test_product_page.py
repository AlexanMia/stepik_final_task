from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time
import pytest


#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019" here alert!!!
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear" here alert!!!
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# случай с перебором сайтов
#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
 #                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
 #                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
 #                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
 #                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
  #                                 pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
  #                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
   #                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#def test_guest_can_add_product_to_basket(browser, link):
#link_to = f"{link}"
#page = ProductPage(browser, link_to)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#page.open()  # открываем страницу
#page.go_to_add_basket()  # выполняем метод страницы — переходим на страницу логина
#login_page = LoginPage(browser, browser.current_url)
#login_page.should_be_login_page()
#time.sleep(2)
#page.solve_quiz_and_get_code()
#time.sleep(120)
#page.should_be_message_about_adding()
#page.should_be_message_basket_total()
#time.sleep(5)


#def test_guest_should_see_button_add(browser, link_to):
#page = ProductPage(browser, link_to)
#page.open()
#page.should_be_button_add_to_basket()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_add_basket()  # выполняем метод страницы — переходим на страницу логина
    #login_page = LoginPage(browser, browser.current_url)
    #login_page.should_be_login_page()
    #time.sleep(2)
    page.solve_quiz_and_get_code()
    #time.sleep(120)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    #time.sleep(5)


def test_guest_should_see_button_add(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_basket()
    #page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_basket()
    #page.solve_quiz_and_get_code()
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.smoke
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(5)

@pytest.mark.regression
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"

    #page = MainPage(browser, link)
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    time.sleep(5)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_things_in_basket()
    basket_page.should_be_note_about_empty_basket()

@pytest.mark.useradd
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, login_link)
        self.page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + 'ffffsff'

        self.page.register_new_user(email, password)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_add_basket()  # выполняем метод страницы — переходим на страницу логина
        # login_page = LoginPage(browser, browser.current_url)
        # login_page.should_be_login_page()
        # time.sleep(2)

        # time.sleep(120)
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()
        # time.sleep(5)