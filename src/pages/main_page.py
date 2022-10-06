from .base_page import BasePage
from .selectors import MainPageSelectors


class MainPage(BasePage):

    def get_enter_button(self):
        button = self.find_element(*MainPageSelectors.ENTER_BUTTON_LOCATOR)
        button.click()
