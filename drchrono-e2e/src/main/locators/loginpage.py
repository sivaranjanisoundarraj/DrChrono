from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """
    This class used to Login Page Locators
    """
    BTN_LOGIN = (By.LINK_TEXT, 'Log In')
    TXT_USERNAME = (By.ID, 'username')
    TXT_PASSWORD = (By.ID, 'password')
    BTN_LOGIN_BUT = (By.ID, 'login')
