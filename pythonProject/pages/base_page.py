import math
from selenium.common import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators


class BasePage():

    def __init__(self, browser, url, timeout=0):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    #метод открытия страниц
    def open(self):
        self.browser.get(self.url)
    #метод перехода на страницу логина/регистрации
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
    #метод открытия корзины незарегистрированным пользователем
    def guest_open_cart(self):
        guest = self.browser.find_element(*BasePageLocators.OPEN_CART)
        guest.click()
    #метод проверки, что присутствует линк на логин/регистрацию
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    #метод проверки, что пользователь зарегистрирован
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
    #проверка, что элемент появляется на странице и не исчезает
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    #проверка, что элемент не появляется на странице в течении заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            wait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    #проверка, что элемент исчезает со страницы
    def is_disappeared(self, how, what, timeout=4):
        try:
            wait(self.browser, timeout, 1).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
    #задача с урока
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
