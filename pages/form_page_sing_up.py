import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
from selenium.webdriver.common.by import By


class FormPageSingUp(BasePage):

    def fill_fields_and_submit(self):
        email = 'wemn2j@yourfastmail.online'
        name = 'Ne'
        password = '1234'
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.NAME).send_keys(name)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.SING_UP).click()

    time.sleep(10)

