from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators

class FormPageSignUp(BasePage):

    def find_sign_up(self):
       assert self.element_is_visible(Locators.SING_UP_HREF).is_displayed()

    def click_sign_up(self):
        self.element_is_visible(Locators.SING_UP_HREF).click()
        cl_sn = self.element_is_visible(Locators.SING_UP_H).text
        assert 'Sign Up' == cl_sn

    def fill_fields_and_submit(self, creds):
        email, name, password = creds
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.NAME).send_keys(name)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.SING_UP).click()
        log_in = self.element_is_visible(Locators.LOGIN_IN_H).text
        assert 'Login' == log_in
    def fill_fields_and_notsign(self, cred):
        email,name, password = cred
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.NAME).send_keys(name)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.SING_UP).click()
        not_sign = self.element_is_visible(Locators.SING_UP_H).text
        assert 'Sign Up' == not_sign
    def email_exists (self, cred):
        email, name, password = cred
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.NAME).send_keys(name)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.SING_UP).click()
        email_exists = self.element_is_visible(Locators.EMAIL_EX).text
        assert 'login page' == email_exists

    def click_login_page(self, cred):
        email, name, password = cred
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.NAME).send_keys(name)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.SING_UP).click()
        self.element_is_visible(Locators.EMAIL_EX).click()
        log_in = self.element_is_visible(Locators.LOGIN_IN_H).text
        assert 'Login' == log_in