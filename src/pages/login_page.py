import time
from selenium.webdriver import Keys
from src.pages.base_page import BasePage
from .constants import AuthData
from .selectors import LoginPageSelectors


class LoginPage(BasePage):
    def enter_login(self):
        login_field = self.find_element(*LoginPageSelectors.LOGIN_FIELD)
        login_field.send_keys(AuthData.login.value)
        login_field.send_keys(Keys.ENTER)

    def enter_pass(self):
        password_field = self.find_element(*LoginPageSelectors.PSWD_FIELD)
        password_field.send_keys(AuthData.password.value)
        password_field.send_keys(Keys.ENTER)
        time.sleep(2) #this sleep need for time for authorization
