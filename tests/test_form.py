import pytest
from pages.form_page import FormPageSignUp
from conftest import driver



class TestFormPage:
    def test_sign_up(self, driver):
        home_page = FormPageSignUp(driver, 'http://localhost:5000')
        home_page.open()
        home_page.find_sign_up()

    def test_sign_up_click(self, driver):
        home_page = FormPageSignUp(driver, 'http://localhost:5000')
        home_page.open()
        home_page.click_sign_up()

    @pytest.mark.parametrize(
        'creds',
        [
            pytest.param(('w3m72z@yourfastmail.online','Anna', 'anna123'), id = 'w3m72z@yourfastmail.online, Anna, anna123'),
            pytest.param(('vcrbb6@yourfastmail.online','', '123$!abs'), id= 'vcrbb6@yourfastmail.online, ,123$!abs'),
            pytest.param(('absd12dfsgjcljahccnbvbvxv@yourfastmail.online', 'Ан', '!&ikfsdvnd'), id='absd12dfsgjcljahccnbvbvxv@yourfastmail.online, Ан, !&ikfsdvnd'),
            pytest.param(('jva23@daymail.site', 'Nana', 'tg0EofHyC'), id='jva23@daymail.site, Nana, tg0EofHyC'),
            pytest.param(('mareteg667@rencr.com', 'liandra', '%eN1c49#7r$%E405'), id='mareteg667@rencr.com, liandra, %eN1c49#7r$%E405')

        ]
    )
    def test_form(self, driver, creds):
        form_page = FormPageSignUp(driver, 'http://localhost:5000/signup')
        form_page.open()
        form_page.fill_fields_and_submit(creds)
    @pytest.mark.parametrize(
        'cred',
        [
            pytest.param(('fv28rk@daymailsite','Andre', '5oe$%s#j96D$61ey'), id ='ffv28rk@daymailsite, Andre, 5oe$%s#j96D$61ey'),
            pytest.param(('f5u27wddaymail.site','NE', 'aaabbbccc'), id='f5u27wddaymail.site,NE , aaabbbccc'),
            pytest.param(('', '', ''), id='empty fields'),
            pytest.param(('hdbvp@.site', '', '123654a'), id='hdbvp@.site, 123654a'),
            pytest.param(('hdbvp@daymail.сит', '', '@oFcr84C~ljp@V9QssI'), id='hdbvp@daymail.сит, @oFcr84C~ljp@V9QssI'),
            pytest.param(('hmuz6m@yourfastmail.online', 'Елена', 'рвздватри'), id='hmuz6m@yourfastmail.online, Елена, рвздватри'),
            pytest.param(('QVHJFv1@yourfastmail.online', '', '@oFcr84C'), id='QVHJFv1@yourfastmail.online, @oFcr84C'),
            pytest.param(('FEZ@DAYMAIL.SITE', 'Lena', 'WTc6aTY7'), id='FEZ@DAYMAIL.SITE, Lena, WTc6aTY7'),
            pytest.param(('hdbvp@.site', '', '123654a'), id='hdbvp@.site, 123654a'),
            pytest.param(('hdbvp@фтлврс.site', '', 'hksndcbf'), id='hdbvp@фтлврс.site, hksndcbf')


        ]
    )
    def test_form_not_sign(self, driver, cred):
        form_page = FormPageSignUp(driver, 'http://localhost:5000/signup')
        form_page.open()
        form_page.fill_fields_and_notsign(cred)
    @pytest.mark.parametrize(
        'cred',
        [
            pytest.param(('w3m72z@yourfastmail.online', 'Anna', 'anna123'), id='w3m72z@yourfastmail.online, Anna, anna123'),
            pytest.param(('vcrbb6@yourfastmail.online', '', '123$!abs'), id='vcrbb6@yourfastmail.online, ,123$!abs'),
            pytest.param(('absd12dfsgjcljahccnbvbvxv@yourfastmail.online', 'Ан', '!&ikfsdvnd'), id='absd12dfsgjcljahccnbvbvxv@yourfastmail.online, Ан, !&ikfsdvnd'),
            pytest.param(('jva23@daymail.site', 'Nana', 'tg0EofHyC'), id='jva23@daymail.site, Nana, tg0EofHyC'),
            pytest.param(('mareteg667@rencr.com', 'liandra', '%eN1c49#7r$%E405'), id='mareteg667@rencr.com, liandra, %eN1c49#7r$%E405')

        ]
    )
    def test_form_email_exists(self, driver, cred):
        form_page = FormPageSignUp(driver, 'http://localhost:5000/signup')
        form_page.open()
        form_page.email_exists(cred)

    @pytest.mark.parametrize(
        'cred',
        [
            pytest.param(('w3m72z@yourfastmail.online', 'Anna', 'anna123'),
                         id='w3m72z@yourfastmail.online, Anna, anna123'),
            pytest.param(('vcrbb6@yourfastmail.online', '', '123$!abs'), id='vcrbb6@yourfastmail.online, ,123$!abs'),
            pytest.param(('absd12dfsgjcljahccnbvbvxv@yourfastmail.online', 'Ан', '!&ikfsdvnd'),
                         id='absd12dfsgjcljahccnbvbvxv@yourfastmail.online, Ан, !&ikfsdvnd'),
            pytest.param(('jva23@daymail.site', 'Nana', 'tg0EofHyC'), id='jva23@daymail.site, Nana, tg0EofHyC'),
            pytest.param(('mareteg667@rencr.com', 'liandra', '%eN1c49#7r$%E405'),
                         id='mareteg667@rencr.com, liandra, %eN1c49#7r$%E405')

        ]
    )
    def test_form_click_login_page(self, driver, cred):
        form_page = FormPageSignUp(driver, 'http://localhost:5000/signup')
        form_page.open()
        form_page.click_login_page(cred)

