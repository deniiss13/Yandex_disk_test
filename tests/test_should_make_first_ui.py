from src.pages.constants import Links
from src.pages import DiskPage
from src.pages import LoginPage
from src.pages import MainPage


def test(browser):
    main_page = MainPage(browser, Links.MAIN_LINK.value)
    main_page.open()
    main_page.get_enter_button()
    login_page = LoginPage(browser)
    login_page.enter_login()
    login_page.enter_pass()
    disk_page = DiskPage(browser, Links.DISK_LINK.value)
    disk_page.open()
    disk_page.copy_object()
    disk_page.delete_object()
