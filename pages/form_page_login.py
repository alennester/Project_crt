import pytest
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPageLogin(BasePage):
    def find_login(self):
        assert self.element_is_visible(Locators.LOGIN_HREF).is_displayed()

    def login_click(self):
        self.element_is_visible(Locators.LOGIN_HREF).click()
        ln_cl = self.element_is_visible(Locators.LOGIN).text
        assert 'Login' == ln_cl

    def fill_fields_and_login(self, users):
        email, password = users
        self.element_is_visible(Locators.EMAIL_LOG).send_keys(email)
        self.element_is_visible(Locators.PASSWORD_LOG).send_keys(password)
        self.element_is_visible(Locators.LOGIN).click()
        assert self.element_is_visible(Locators.PROFILE).is_displayed()


    def fill_fields_check_login(self, users):
        email, password = users
        self.element_is_visible(Locators.EMAIL_LOG).send_keys(email)
        self.element_is_visible(Locators.PASSWORD_LOG).send_keys(password)
        self.element_is_visible(Locators.CHECK_BOX).click()
        self.element_is_visible(Locators.LOGIN).click()
        assert self.element_is_visible(Locators.PROFILE).is_displayed()


    def fill_email_warning(self, try_again):
        email, password = try_again
        self.element_is_visible(Locators.EMAIL_LOG).send_keys(email)
        self.element_is_visible(Locators.PASSWORD_LOG).send_keys(password)
        self.element_is_visible(Locators.LOGIN).click()
        login = self.element_is_visible(Locators.TRY_AGAIN).text
        assert 'Please check your login details and try again.' == login

    def fill_field_and_login(self, log):
        email, password = log
        self.element_is_visible(Locators.EMAIL_LOG).send_keys(email)
        self.element_is_visible(Locators.PASSWORD_LOG).send_keys(password)
        self.element_is_visible(Locators.LOGIN).click()
        login = self.element_is_visible(Locators.LOGIN_IN_H).text
        assert 'Login' == login

    def check_login(self, log_check):
        email, password = log_check
        self.element_is_visible(Locators.EMAIL_LOG).send_keys(email)
        self.element_is_visible(Locators.PASSWORD_LOG).send_keys(password)
        self.element_is_visible(Locators.CHECK_BOX).click()
        self.element_is_visible(Locators.LOGIN).click()
        login = self.element_is_visible(Locators.LOGIN_IN_H).text
        assert 'Login' == login
