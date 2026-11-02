import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import shutil


@pytest.fixture
def driver():
    geckodriver_path = shutil.which("geckodriver")
    service = Service(executable_path=geckodriver_path)
    browser = webdriver.Firefox(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()

