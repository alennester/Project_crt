from pages.form_page_login import FormPageLogin
from conftest import driver


class TestFormPageLogin:
    def test_form(self, driver):
        form_page = FormPageLogin(driver, 'http://localhost:5000/login')
        form_page.open()
        form_page.fill_fields_and_login()
