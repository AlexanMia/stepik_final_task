from .pages.product_page import ProductPage
import time
import pytest


#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"



#@pytest.mark.parametrize('link', ["okay_link", pytest.param("bugged_link", marks=pytest.mark.xfail), "okay_link"])

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link_to = f"{link}"
    page = ProductPage(browser, link_to)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_add_basket()  # выполняем метод страницы — переходим на страницу логина
    #login_page = LoginPage(browser, browser.current_url)
    #login_page.should_be_login_page()

    page.solve_quiz_and_get_code()
    #time.sleep(120)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    time.sleep(10)


#def test_guest_should_see_button_add(browser, link):

    #page = ProductPage(browser, link)
    #page.open()
    #page.should_be_button_add_to_basket()






