from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    OPEN_CART = (By.CSS_SELECTOR, 'span .btn.btn-default[href]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_PRODUCT_TO_CART = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6 h1')
    NAME_OF_PRODUCT_ADDED = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    MESSAGE_PRICE_ADDED_PRODUCT_IN_CART = (By.CSS_SELECTOR, '.alertinner p strong')
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6 p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert.alert-success div.alertinner')



class CartPageLocators():
    MESSAGE_PRODUCT_IN_CART = (By.CSS_SELECTOR, 'h2.col-sm-6')
    MESSAGE_YOUR_CART_IS_EMPTY = (By.CSS_SELECTOR, 'div #content_inner')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    ENTER_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    ENTER_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    ENTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[value="Log In"]')
    FORGOT_PASSWORD = (By.CSS_SELECTOR, 'a[href*="password-reset"]')

    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_NEW_USER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_NEW_USER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_NEW_USER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')
