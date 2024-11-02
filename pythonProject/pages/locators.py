from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    #Зарегистрированный пользователь
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    ENTER_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    ENTER_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    ENTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[value="Log In"]')
    FORGOT_PASSWORD = (By.CSS_SELECTOR, 'a[href="/ru/password-reset/"]')
    #Новый пользователь
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_NEW_USER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_NEW_USER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_NEW_USER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')



