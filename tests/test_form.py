import time
import pytest
from pages.form_page import FormPageSignUp
from conftest import driver


class TestFormPage:
    def test_sign_up(self, driver):
        home_page = FormPageSignUp(driver, 'http://localhost:5000')
        home_page.open()
        home_page.find_sign_up()

    def test_sign_up(self, driver):
        home_page = FormPageSignUp(driver, 'http://localhost:5000')
        home_page.open()
        home_page.click_sign_up()

    @pytest.mark.parametrize(
        'creds',
        [
            pytest.param(('wx@daymail.site','', '1234'), id ='fv28rk@daymail.site,,1234'),
            # pytest.param(('sporn@yourfastmail.online','Anna', 'aaabbbccc'), id='f5u27wd@daymail.site,Анна,aaabbbccc'),
            # pytest.param(('', '', ''), id=',,'),
            # pytest.param(('', '', ''), id=',,'),
            # pytest.param(('', '', ''), id=',,')

        ]
    )
    def test_form(self, driver, creds):
        form_page = FormPageSignUp(driver, 'http://localhost:5000/signup')
        form_page.open()
        form_page.fill_fields_and_submit(creds)
    @pytest.mark.parametrize(
        'cred',
        [
            pytest.param(('fv28rk@daymail.site','', '1234'), id ='fv28rk@daymail.site,,1234'),
            pytest.param(('f5u27wd@daymail.site','NE', 'aaabbbccc'), id='f5u27wd@daymail.site,Анна,aaabbbccc'),
            # pytest.param(('', '', ''), id=',,'),
            # pytest.param(('', '', ''), id=',,'),
            # pytest.param(('', '', ''), id=',,')

        ]
    )
    def test_form_not_sign(self, driver, cred):
        form_page = FormPageSignUp(driver, 'http://localhost:5000/signup')
        form_page.open()
        form_page.fill_fields_and_notsign(cred)
    @pytest.mark.parametrize(
        'cred',
        [
            pytest.param(('fv28rk@daymail.site', '', '1234'), id='fv28rk@daymail.site,,1234'),
            # pytest.param(('f5u27wd@daymail.site', 'NE', 'aaabbbccc'), id='f5u27wd@daymail.site,Анна,aaabbbccc'),
            # pytest.param(('', '', ''), id=',,'),
            # pytest.param(('', '', ''), id=',,'),
            # pytest.param(('', '', ''), id=',,')

        ]
    )
    def test_form_email_exists(self, driver, cred):
        form_page = FormPageSignUp(driver, 'http://localhost:5000/signup')
        form_page.open()
        form_page.email_exists(cred)

    @pytest.mark.parametrize(
        'cred',
        [
            pytest.param(('fv28rk@daymail.site', '', '1234'), id='fv28rk@daymail.site,,1234'),
            # pytest.param(('f5u27wd@daymail.site', 'NE', 'aaabbbccc'), id='f5u27wd@daymail.site,Анна,aaabbbccc'),
            # pytest.param(('', '', ''), id=',,'),
            # pytest.param(('', '', ''), id=',,'),
            # pytest.param(('', '', ''), id=',,')

        ]
    )
    def test_form_click_login_page(self, driver, cred):
        form_page = FormPageSignUp(driver, 'http://localhost:5000/signup')
        form_page.open()
        form_page.click_login_page(cred)

