from selenium.webdriver.common.by import By


class FormPageLocators:
    EMAIL = (By.XPATH, '/html/body/section/div[2]/div/div/div/form/div[1]/div/input')
    NAME = (By.XPATH, '/html/body/section/div[2]/div/div/div/form/div[2]/div/input')
    PASSWORD = (By.XPATH, '/html/body/section/div[2]/div/div/div/form/div[3]/div/input')
    SING_UP_HREF = (By.XPATH, '//*[@id="navbarMenuHeroA"]/div/a[3]')
    LOGIN_HREF = (By.XPATH, '//*[@id="navbarMenuHeroA"]/div/a[2]')
    SING_UP = (By.XPATH, '/html/body/section/div[2]/div/div/div/form/button')
    LOGIN = (By.XPATH, '/html/body/section/div[2]/div/div/div/form/button')
    EMAIL_LOG = (By.XPATH, '/html/body/section/div[2]/div/div/div/form/div[1]/div/input')
    PASSWORD_LOG = (By.XPATH, '/html/body/section/div[2]/div/div/div/form/div[2]/div/input')
