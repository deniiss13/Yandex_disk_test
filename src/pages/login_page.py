import time

from selenium.webdriver import Keys

from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .constants import AuthData
from .selectors import LoginPageSelectors


class LoginPage(BasePage):
    def enter_login(self):
        login_field = self.browser.find_element(By.ID, LoginPageSelectors.LOGIN_FIELD.value)
        login_field.send_keys(AuthData.login.value)
        login_field.send_keys(Keys.ENTER)

    def enter_pass(self):
        password_field = self.browser.find_element(By.ID, LoginPageSelectors.PSWD_FIELD.value)
        password_field.send_keys(AuthData.password.value)
        password_field.send_keys(Keys.ENTER)
        time.sleep(2)
