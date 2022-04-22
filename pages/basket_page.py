from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_things_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Items is in the basket, but should not be"

    def should_be_note_about_empty_basket(self):
        # реализуйте проверку, что есть запись про пустую корзину
        assert self.is_element_present(*BasketPageLocators.NOTE_ABOUT_BASKET), "No note about empty basket"


