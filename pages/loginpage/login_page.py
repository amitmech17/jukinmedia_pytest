import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username_field = "#username"
    _password_field = "//input[@id='creds.password']"
    _login_button = "//input[@id='loginButton']"
    _invalid_email_password = "//div[contains(text(),'Incorrect email/password combination')]"

    def enterUsername(self, username):
        self.sendKeys(username, self._username_field, locatorType="css")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, username, password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginPageTitle(self):
        return self.verifyPageTitle("Login Page")

    def successLoginPageTitle(self):
        return self.verifyPageTitle("Login Success")

    def invalidpass(self):
        if self.isElementPresent(self._invalid_email_password, locatorType="xpath"):
            return True
        else:
            return False