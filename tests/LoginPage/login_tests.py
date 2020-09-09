from pages.loginpage.login_page import LoginPage
from utilities.test_status import Status
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)


    # @pytest.mark.run(order=2)
    def test_t1validLogin(self):
        self.log.info("test_t1validLogin started")
        login_page_title_result = self.lp.verifyLoginPageTitle()
        self.ts.mark(login_page_title_result,"Login Page Verification")
        self.lp.login("quality@jukinmedia.com","Test1ng")
        login_success_result = self.lp.successLoginPageTitle()
        self.ts.markFinal("test_t1validLogin",login_success_result,"Login success verification")

    # @pytest.mark.run(order=1)
    def test_t2invalidLogin(self):
        self.log.info("test_t2invalidLogin started")
        login_page_title_result = self.lp.verifyLoginPageTitle()
        self.ts.mark(login_page_title_result, "Login Page Verification")
        self.lp.login("test@test.com", "wrong")
        invalidlogin_success_result = self.lp.invalidpass()
        self.ts.markFinal("test_t2invalidLogin", invalidlogin_success_result, "incorrect Login credentials message verification")