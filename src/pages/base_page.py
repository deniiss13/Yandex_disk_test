import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, url=None, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find_element(self, locator_strategy, locator):
        try:
            wait = WebDriverWait(self.browser, 5)
            wait.until(EC.visibility_of_element_located((locator_strategy, locator)))
            return self.browser.find_element(locator_strategy, locator)
        except TimeoutException:
            logging.warning(f"Can't find element with Explicit Wait, file={locator}")
            return False

    def find_elements(self, locator_strategy, locator):
        try:
            wait = WebDriverWait(self.browser, 5)
            wait.until(EC.visibility_of_any_elements_located((locator_strategy, locator)))
            return self.browser.find_elements(locator_strategy, locator)
        except TimeoutException:
            logging.warning(f"Can't find element with Explicit Wait, file={locator}")
            return False


