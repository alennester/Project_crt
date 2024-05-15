import time
import pytest
from pages.form_page_login import FormPageLogin
from conftest import driver
from selenium.webdriver.common.by import By


class TestFormPageLogin:
    def test_find_login(self, driver):
        login_href = FormPageLogin(driver, 'http://localhost:5000')
        login_href.open()
        login_href.find_login()

    def test_login_click(self, driver):
        login_href = FormPageLogin(driver, 'http://localhost:5000')
        login_href.open()
        login_href.login_click()

    @pytest.mark.parametrize(
        'users',
        [
            pytest.param(('w3m72z@yourfastmail.online', 'anna123'), id='w3m72z@yourfastmail.online, anna123'),
            pytest.param(('vcrbb6@yourfastmail.online', '123$!abs'), id='vcrbb6@yourfastmail.online, 123$!abs'),
            pytest.param(('absd12dfsgjcljahccnbvbvxv@yourfastmail.online', '!&ikfsdvnd'), id='absd12dfsgjcljahccnbvbvxv@yourfastmail.online,!&ikfsdvnd'),
            pytest.param(('jva23@daymail.site', 'tg0EofHyC'), id='jva23@daymail.site,tg0EofHyC'),
            pytest.param(('mareteg667@rencr.com', '%eN1c49#7r$%E405'), id='mareteg667@rencr.com,%eN1c49#7r$%E405')

        ]
    )
    def test_form(self, driver, users):
        form_page = FormPageLogin(driver, 'http://localhost:5000/login')
        form_page.open()
        form_page.fill_fields_and_login(users)

    @pytest.mark.parametrize(
        'users',
        [
            pytest.param(('w3m72z@yourfastmail.online', 'anna123'),
                         id='w3m72z@yourfastmail.online, anna123'),
            pytest.param(('vcrbb6@yourfastmail.online', '123$!abs'), id='vcrbb6@yourfastmail.online, 123$!abs'),
            pytest.param(('absd12dfsgjcljahccnbvbvxv@yourfastmail.online', '!&ikfsdvnd'),
                         id='absd12dfsgjcljahccnbvbvxv@yourfastmail.online,!&ikfsdvnd'),
            pytest.param(('jva23@daymail.site', 'tg0EofHyC'), id='jva23@daymail.site,tg0EofHyC'),
            pytest.param(('mareteg667@rencr.com', '%eN1c49#7r$%E405'),
                         id='mareteg667@rencr.com,%eN1c49#7r$%E405')
        ]
    )
    def test_form_check(self, driver, users):
        form_page = FormPageLogin(driver, 'http://localhost:5000/login')
        form_page.open()
        form_page.fill_fields_check_login(users)

    @pytest.mark.parametrize(
        'try_again',
        [
            pytest.param(('w3m72z@yourfastmail.online', '12345'), id='w3m72z@yourfastmail.online, 12345'),
            pytest.param(('vcrbb6@yourfastmail.online', 'aaabbbcccfd'), id='vcrbb6@yourfastmail.online, aaabbbcccfd'),
            pytest.param(('2f2ez@daymail.site', ''), id='2f2ez@daymail.site'),
            pytest.param(('jva23@daymail.site', ''), id='jva23@daymail.site'),

        ]
    )
    def test_form_warning(self, driver, try_again):
        form_page = FormPageLogin(driver, 'http://localhost:5000/login')
        form_page.open()
        form_page.fill_email_warning(try_again)

    @pytest.mark.parametrize(
        'log',
        [
            pytest.param(('fv28rk@daymailsite', '5oe$%s#j96D$61ey'), id='ffv28rk@daymailsite, 5oe$%s#j96D$61ey'),
            pytest.param(('f5u27wddaymail.site', 'aaabbbccc'), id='f5u27wddaymail.site, aaabbbccc'),
            pytest.param(('', ''), id='empty fields'),
            pytest.param(('hdbvp@.site', '123654a'), id='hdbvp@.site, 123654a'),
            pytest.param(('hdbvp@daymail.сит', '@oFcr84C~ljp@V9QssI'), id='hdbvp@daymail.сит, @oFcr84C~ljp@V9QssI'),
            pytest.param(('hmuz6m@yourfastmail.online', 'рвздватри'), id='hmuz6m@yourfastmail.online, рвздватри'),
            pytest.param(('QVHJFv1@yourfastmail.online', '@oFcr84C'), id='QVHJFv1@yourfastmail.online, @oFcr84C'),
            pytest.param(('FEZ@DAYMAIL.SITE', 'WTc6aTY7'), id='FEZ@DAYMAIL.SITE, WTc6aTY7'),
            pytest.param(('hdbvp@фтлврс.site', 'hksndcbf'), id='hdbvp@фтлврс.site, hksndcbf')
        ]
    )
    def test_form_login(self, driver, log):
        form_page = FormPageLogin(driver, 'http://localhost:5000/login')
        form_page.open()
        form_page.fill_field_and_login(log)
    @pytest.mark.parametrize(
        'log_check',
        [
            pytest.param(('fv28rk@daymailsite', '5oe$%s#j96D$61ey'), id='ffv28rk@daymailsite, 5oe$%s#j96D$61ey'),
            pytest.param(('f5u27wddaymail.site', 'aaabbbccc'), id='f5u27wddaymail.site, aaabbbccc'),
            pytest.param(('', ''), id='empty fields'),
            pytest.param(('hdbvp@.site', '123654a'), id='hdbvp@.site, 123654a'),
            pytest.param(('hdbvp@daymail.сит', '@oFcr84C~ljp@V9QssI'), id='hdbvp@daymail.сит, @oFcr84C~ljp@V9QssI'),
            pytest.param(('hmuz6m@yourfastmail.online', 'рвздватри'), id='hmuz6m@yourfastmail.online, рвздватри'),
            pytest.param(('QVHJFv1@yourfastmail.online', '@oFcr84C'), id='QVHJFv1@yourfastmail.online, @oFcr84C'),
            pytest.param(('FEZ@DAYMAIL.SITE', 'WTc6aTY7'), id='FEZ@DAYMAIL.SITE, WTc6aTY7'),
            pytest.param(('hdbvp@фтлврс.site', 'hksndcbf'), id='hdbvp@фтлврс.site, hksndcbf')
        ]
    )
    def test_form_login(self, driver, log_check):
        form_page = FormPageLogin(driver, 'http://localhost:5000/login')
        form_page.open()
        form_page.check_login(log_check)