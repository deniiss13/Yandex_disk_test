from selenium import webdriver
from src.back import Client
import pytest


@pytest.fixture(scope="function")
def client():
    return Client()


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.close()
