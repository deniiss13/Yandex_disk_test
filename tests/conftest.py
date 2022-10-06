from selenium import webdriver
from src.pages.disk_page import DiskPage
from src.back import Client
import pytest


@pytest.fixture(scope="function")
def client():
    return Client()


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    disk_page = DiskPage(browser)
    disk_page.log_out()
    browser.quit()
