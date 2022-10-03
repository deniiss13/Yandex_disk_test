from selenium.webdriver.common.by import By
from .base_page import BasePage
from .selectors import MainPageSelectors


class MainPage(BasePage):

    def get_enter_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, MainPageSelectors.ENTER_BUTTON_CLASS.value)
