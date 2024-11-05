from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductBooksPage(BasePage):

    def should_be_add_product_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_CART)
        add_to_cart.click()

    def check_product_name_add_to_cart(self):
        check_product = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_CHECK)
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        assert check_product.text == name_of_product.text, (f'Product {check_product.text} has not been added to cart.'
                                                            f'Expected "{name_of_product.text}"')

    def check_price_product(self):
        check_message_of_added_product = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_ADDED_PRODUCT_IN_CART)
        check_price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT)
        assert check_message_of_added_product.text == check_price_of_product.text,\
            (f'The price of the added item "{check_message_of_added_product.text}"'
             f' does not match the price of the product "{check_price_of_product.text}".')