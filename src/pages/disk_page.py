from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from src.pages.base_page import BasePage
from .selectors import DiskPageSelectors
from .constants import Names, Path


class DiskPage(BasePage):
    def copy_object(self):
        copy_item = self.find_elements(*DiskPageSelectors.COPY_ITEM)[2]
        copy_item.click()
        copy_button = self.find_element(*DiskPageSelectors.COPY_BUTTON)
        copy_button.click()
        new_folder = self.find_element(*DiskPageSelectors.NEW_FOLDER)
        new_folder.click()
        copy_button_window = self.find_element(*DiskPageSelectors.COPY_BUTTON_WINDOW)
        copy_button_window.click()

    def delete_object(self):
        drag_item = self.browser.find_elements(*DiskPageSelectors.DRAG_ITEM)[3]
        drop_item = self.find_element(*DiskPageSelectors.DROP_ITEM)
        ActionChains(self.browser).drag_and_drop(drag_item, drop_item).perform()
        folder = self.find_element(*DiskPageSelectors.FOLDER)
        ActionChains(self.browser).double_click(on_element=folder).perform()
        self.find_elements(*DiskPageSelectors.DELETE_ITEM)[1].click()
        delete_button = self.find_element(*DiskPageSelectors.DELETE_BUTTON)
        delete_button.click()

    def log_out(self):
        user_icon = self.find_element(*DiskPageSelectors.USER_ICON)
        user_icon.click()
        user_exit = self.find_element(*DiskPageSelectors.USER_EXIT)
        user_exit.click()

    def create_folder(self):
        add = self.browser.find_element(*DiskPageSelectors.CREATE)
        add.click()
        add_folder = self.find_element(*DiskPageSelectors.ADD_FOLDER)
        add_folder.click()

    def name_folder(self):
        folder_name = self.find_element(*DiskPageSelectors.NAME_FIELD)
        folder_name.send_keys(Names.NEW_FOLDER.value)
        folder_name.send_keys(Keys.ENTER)

    def open_folder(self):
        folder_open = self.find_elements(*DiskPageSelectors.COPY_ITEM)[2]
        ActionChains(self.browser).double_click(on_element=folder_open).perform()

    def upload_file(self):
        get_file = self.find_element(*DiskPageSelectors.UPLOAD_FIELD)
        get_file.send_keys(Path.UPLOAD_FILE.value)

    def check_text(self):
        open_file = self.browser.find_element1(*DiskPageSelectors.FOLDER)
        ActionChains(self.browser).double_click(on_element=open_file).perform()
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        text_find = self.find_element(*DiskPageSelectors.TEXT_IN_FILE)
        assert Path.CORRECT_TEXT.value in text_find.text

    def first_window(self):
        new_window = self.browser.window_handles[0]
        self.browser.switch_to.window(new_window)





