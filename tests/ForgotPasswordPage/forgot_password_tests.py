from pages.forgotpassword.forgot_password import ForgotPasswordPage
from pages.loginpage.login_page import LoginPage
from utilities.test_status import Status
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time


@pytest.mark.usefixtures("oneTimeSetUp")
class ForgotPasswordTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.forgot = ForgotPasswordPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    # @pytest.mark.run(order=2)
    def test_t9valid_email_ForgotPassword(self):
        self.log.info("test_t9valid_email_ForgotPassword success")
        self.forgot.forgotpasswordLoginPageButton()
        forgot_password_page_title_result = self.forgot.verifyForgotPasswordPageTitle()
        self.ts.mark(forgot_password_page_title_result,"Forgot Password Page Verification")
        self.forgot.forgotPassword("quality@jukinmedia.com")
        forgot_password_success_result = self.forgot.successForgotPassword()
        self.ts.markFinal("test_t9valid_email_ForgotPassword",forgot_password_success_result,"Forgot Password success verification")

    # @pytest.mark.run(order=1)
    def test_t10invalid_email_ForgotPassword(self):
        self.log.info("test_t10invalid_email_ForgotPassword started")
        self.forgot.forgotpasswordLoginPageButton()
        forgot_password_page_title_result = self.forgot.verifyForgotPasswordPageTitle()
        self.ts.mark(forgot_password_page_title_result, "Forgot password Page Verification")
        self.forgot.forgotPassword("quality")
        time.sleep(2)
        invalid_email_message = self.forgot.invalidEmail()
        self.ts.markFinal("test_t10invalid_email_ForgotPassword", invalid_email_message, "invalid email message verification")

    def test_t11back_to_login_page(self):
        self.log.info("test_t11back_to_login_page")
        self.forgot.forgotpasswordLoginPageButton()
        forgot_password_page_title_result = self.forgot.verifyForgotPasswordPageTitle()
        self.ts.mark(forgot_password_page_title_result, "Forgot password Page Verification")
        self.forgot.backtologin()
        time.sleep(2)
        login_page_title = self.lp.verifyLoginPageTitle()
        self.ts.markFinal("test_t11back_to_login_page", login_page_title, "Back to login Page verification")