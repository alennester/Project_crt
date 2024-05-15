import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
