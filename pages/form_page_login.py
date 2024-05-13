import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPageLogin(BasePage):
    def fill_fields_and_login(self):
        email = 'md3t0kd@yourfastmail.online'
        name = 'Ne'
        password = '1234'
        self.element_is_visible(Locators.EMAIL_LOG).send_keys(email)
        self.element_is_visible(Locators.PASSWORD_LOG).send_keys(password)
        self.element_is_visible(Locators.LOGIN).click()

    time.sleep(10)


