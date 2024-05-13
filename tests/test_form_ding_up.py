from pages.form_page_sing_up import FormPageSingUp
from conftest import driver
from selenium.webdriver.common.by import By


class TestFormPage:
    def test_sing_up(self, driver):
        form_page = FormPageSingUp(driver, 'http://localhost:5000')
        form_page.open()
        assert driver.find_element(By.XPATH, '//*[@id="navbarMenuHeroA"]/div/a[3]').is_displayed()

    def test_form(self, driver):
        form_page = FormPageSingUp(driver, 'http://localhost:5000/signup')
        form_page.open()
        form_page.fill_fields_and_submit()
