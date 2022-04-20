from .pages.product_page import ProductPage
import time



def test_guest_should_see_button_add(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_add_basket()  # выполняем метод страницы — переходим на страницу логина
    #login_page = LoginPage(browser, browser.current_url)
    #login_page.should_be_login_page()

    page.solve_quiz_and_get_code()
    time.sleep(20)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()









