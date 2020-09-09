import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class ForgotPasswordPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _email_field = "//input[@id='fp.email']"
    _submit_button = "//a[@id='forgotPasswordButton']"
    _back_to_login_button = "//a[contains(text(),'Back to Login')]"
    _forgot_password_reset_success = "//h5[@id='fpSuccessModalLabel']"
    _invalid_email_address = "//div[@id='flashMsg']"
    _forgot_password_login_page = "//a[contains(text(),'Forgot Password?')]"
    _back_to_login = "//a[contains(text(),'Back to Login')]"


    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def clickSubmitButton(self):
        self.elementClick(self._submit_button, locatorType="xpath")

    def forgotpasswordLoginPageButton(self):
        self.elementClick(self._forgot_password_login_page, locatorType="xpath")

    def backtologin(self):
        self.elementClick(self._back_to_login, locatorType="xpath")

    def forgotPassword(self, email):
        self.enterEmail(email)
        self.clickSubmitButton()

    def verifyForgotPasswordPageTitle(self):
        return self.verifyPageTitle("Forgot Password")

    def successForgotPassword(self):
        if "Password reset successfully" in self.getText(self._forgot_password_reset_success, locatorType="xpath"):
            return True
        else:
            return False


    def invalidEmail(self):
        if "Please enter a valid email" in self.getText(self._invalid_email_address, locatorType="xpath"):
            return True
        else:
            return False


