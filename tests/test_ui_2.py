from src.pages.constants import Links
from src.pages.disk_page import DiskPage
from src.pages.login_page import LoginPage
from src.pages import MainPage


def test(browser):
    main_page = MainPage(browser, Links.MAIN_LINK.value)
    main_page.open()
    button = main_page.get_enter_button()
    button.click()
    login_page = LoginPage(browser)
    login_page.enter_login()
    login_page.enter_pass()
    disk_page = DiskPage(browser, Links.DISK_LINK.value)
    disk_page.open()
    disk_page.create_folder()
    disk_page.name_folder()
    disk_page.open_folder()
    disk_page.upload_file()
    disk_page.check_text()
    disk_page.first_window()
    disk_page = DiskPage(browser, Links.DISK_LINK.value)
    disk_page.open()
    disk_page.log_out()
