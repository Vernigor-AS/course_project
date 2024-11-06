from pages.base_page import BasePage
from pages.locators import CartPageLocators


class BasketPage(BasePage):

    def check_that_there_are_no_items_in_the_cart(self):
        assert self.is_not_element_present(*CartPageLocators.MESSAGE_PRODUCT_IN_CART)
        "Items are present in the cart, but should not be."

    def check_the_message_about_the_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.MESSAGE_YOUR_CART_IS_EMPTY)
        "Empty basket message is not presented."
