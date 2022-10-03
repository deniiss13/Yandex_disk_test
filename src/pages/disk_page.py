import time
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from .selectors import DiskPageSelectors
from .constants import *


class DiskPage(BasePage):
    def copy_object(self):
        copy_item = self.browser.find_elements(By.CSS_SELECTOR, DiskPageSelectors.COPY_ITEM.value)[2]
        copy_item.click()
        time.sleep(1)
        copy_button = self.browser.find_element(By.CSS_SELECTOR, DiskPageSelectors.COPY_BUTTON.value)
        copy_button.click()
        time.sleep(1)
        new_folder = self.browser.find_element(By.XPATH, DiskPageSelectors.NEW_FOLDER.value)
        new_folder.click()
        time.sleep(1)
        copy_button_window = self.browser.find_element(By.CSS_SELECTOR, DiskPageSelectors.COPY_BUTTON_WINDOW.value)
        copy_button_window.click()
        time.sleep(1)

    def delete_object(self):
        drag_item = self.browser.find_elements(By.CSS_SELECTOR, DiskPageSelectors.DRAG_ITEM.value)[3]
        drop_item = self.browser.find_element(By.CSS_SELECTOR, DiskPageSelectors.DROP_ITEM.value)
        ActionChains(self.browser).drag_and_drop(drag_item, drop_item).perform()
        time.sleep(1)
        folder = self.browser.find_element(By.CSS_SELECTOR, DiskPageSelectors.FOLDER.value)
        ActionChains(self.browser).double_click(on_element=folder).perform()
        time.sleep(1)
        delete_item = self.browser.find_elements(By.CSS_SELECTOR, DiskPageSelectors.DELETE_ITEM.value)[1]
        delete_item.click()
        time.sleep(1)
        delete_button = self.browser.find_element(By.CSS_SELECTOR, DiskPageSelectors.DELETE_BUTTON.value)
        delete_button.click()

    def log_out(self):
        user_icon = self.browser.find_element(By.CSS_SELECTOR, DiskPageSelectors.USER_ICON.value)
        user_icon.click()
        time.sleep(2)
        user_exit = self.browser.find_element(By.CSS_SELECTOR,DiskPageSelectors.USER_EXIT.value)
        user_exit.click()
        time.sleep(2)

    def create_folder(self):
        add = self.browser.find_element(By.CSS_SELECTOR, DiskPageSelectors.CREATE.value)
        add.click()
        add_folder = self.browser.find_element(By.CSS_SELECTOR, DiskPageSelectors.ADD_FOLDER.value)
        add_folder.click()
        time.sleep(1)

    def name_folder(self):
        folder_name = self.browser.find_element(By.CSS_SELECTOR, DiskPageSelectors.NAME_FIELD.value)
        folder_name.send_keys(Names.NEW_FOLDER.value)
        folder_name.send_keys(Keys.ENTER)
        time.sleep(1)

    def open_folder(self):
        folder_open = self.browser.find_elements(By.CSS_SELECTOR, DiskPageSelectors.COPY_ITEM.value)[2]
        ActionChains(self.browser).double_click(on_element=folder_open).perform()
        time.sleep(1)

    def upload_file(self):
        get_file = self.browser.find_element(By.CSS_SELECTOR, DiskPageSelectors.UPLOAD_FIELD.value)
        get_file.send_keys(Path.UPLOAD_FILE.value)
        time.sleep(2)

    def check_text(self):
        open_file = self.browser.find_element(By.CSS_SELECTOR, DiskPageSelectors.FOLDER.value)
        ActionChains(self.browser).double_click(on_element=open_file).perform()
        time.sleep(1)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        text_find = self.browser.find_element(By.XPATH, DiskPageSelectors.TEXT_IN_FILE.value)
        assert Path.CORRECT_TEXT.value in text_find.text
        time.sleep(1)

    def first_window(self):
        new_window = self.browser.window_handles[0]
        self.browser.switch_to.window(new_window)





