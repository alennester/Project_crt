import time

from pages.form_page_login import FormPageLogin
from conftest import driver
from selenium.webdriver.common.by import By


class TestFormPageLogin:
    def test_login(self, driver):
        login_href = FormPageLogin(driver, 'http://localhost:5000')
        login_href.open()
        assert driver.find_element(By.XPATH, '//*[@id="navbarMenuHeroA"]/div/a[2]').is_displayed()

    def test_form(self, driver):
        form_page = FormPageLogin(driver, 'http://localhost:5000/login')
        form_page.open()
        form_page.fill_fields_and_login()
        assert 'Profile' == driver.find_element(By.XPATH, '//*[@id="navbarMenuHeroA"]/div/a[2]').text
    def test_form_login(self, driver):
        form_page = FormPageLogin(driver, 'http://localhost:5000/login')
        form_page.open()
        form_page.fill_field_and_login()
        assert 'Login' == driver.find_element(By.XPATH, '/html/body/section/div[2]/div/div/h3').text
        time.sleep(5)