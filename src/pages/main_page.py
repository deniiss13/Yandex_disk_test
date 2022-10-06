from .base_page import BasePage
from .selectors import MainPageSelectors


class MainPage(BasePage):

    def get_enter_button(self):
        self.find_element(*MainPageSelectors.ENTER_BUTTON_LOCATOR).click()
