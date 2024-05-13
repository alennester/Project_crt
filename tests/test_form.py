from pages.form_page_sing_up import FormPageSingUp
from conftest import driver
from selenium.webdriver.common.by import By


class TestFormPage:
    def test_sing_up(self, driver):
        home_page = FormPageSingUp(driver, 'http://localhost:5000')
        home_page.open()
        assert driver.find_element(By.XPATH, '//*[@id="navbarMenuHeroA"]/div/a[3]').is_displayed()


    def test_form(self, driver):
        form_page = FormPageSingUp(driver, 'http://localhost:5000/signup')
        form_page.open()
        form_page.fill_fields_and_submit()
        assert 'Login' == driver.find_element(By.XPATH, '/html/body/section/div[2]/div/div/h3').text