import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class RegisterPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _register_button_loginpage = "//a[contains(text(),'Register')]"
    _email_field = "//input[@id='reg.email']"
    _password_field = "//input[@id='reg.password']"
    _confirm_password_field = "//input[@id='reg.confirmPassword']"
    _register_button_registerpage = "//input[@name='_action_doRegister']"
    _back_button = "//input[@name='_action_index']"
    _failed_message = "//div[@id='failedMessage']"
    _tooltip = "//img[@id='tooltipImg']"
    _tooltip_content = "//div[@class='ui-tooltip-content']"

    def enteremail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def confirmPassword(self, password):
        self.sendKeys(password, self._confirm_password_field, locatorType="xpath")

    def clickregisterButton(self):
        self.elementClick(self._register_button_registerpage, locatorType="xpath")

    def clickregisterButtonLogin(self):
        self.elementClick(self._register_button_loginpage, locatorType="xpath")

    def hintbuttonclick(self):
        self.elementClick(self._tooltip, locatorType="xpath")

    def register(self, email, password):
        self.enteremail(email)
        self.enterPassword(password)
        self.confirmPassword(password)
        self.clickregisterButton()

    def register_blank_values(self):
        self.clickregisterButton()

    def registerWithConfirmPasswordBlank(self, email, password):
        self.enteremail(email)
        self.enterPassword(password)
        self.clickregisterButton()

    def verifyregisterPageTitle(self):
        return self.verifyPageTitle("Registration")

    def successRegisterPageTitle(self):
        return self.verifyPageTitle("Registration Successful")


    def invalidEmail(self):
        if "Please enter a valid Email" in self.getText(self._failed_message, locatorType="xpath"):
            return True
        else:
            return False

    def fillAllDetail(self):
        if "Please fill out all fields" in self.getText(self._failed_message, locatorType="xpath"):
            return True
        else:
            return False

    def confirmPasswordBlank(self):
        if "Password confirmation must must match Password" in self.getText(self._failed_message, locatorType="xpath"):
            return True
        else:
            return False

    def tooltipcontent(self):
        if "Password must be at least 8 characters" in self.getText(self._tooltip_content, locatorType="xpath"):
            return False
        else:
            return True