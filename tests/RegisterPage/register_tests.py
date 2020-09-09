from pages.registerpage.register_page import RegisterPage
from utilities.test_status import Status
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time


@pytest.mark.usefixtures("oneTimeSetUp")
class RegisterTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.rp = RegisterPage(self.driver)
        self.ts = Status(self.driver)

    # @pytest.mark.run(order=2)
    def test_t3_valid_Registration(self):
        self.log.info("test_t3validRegistration started")
        self.rp.clickregisterButtonLogin()
        register_page_title_result = self.rp.verifyregisterPageTitle()
        self.ts.mark(register_page_title_result,"Registration Page Verification")
        self.rp.register("amitmech17@gmail.com","Dream@1234")
        time.sleep(1)
        register_success_result = self.rp.successRegisterPageTitle()
        self.ts.markFinal("test_t3validRegistration",register_success_result,"Registration success verification")

    # @pytest.mark.run(order=1)
    #invalid registartion by not using password that is decribed in hint text
    def test_t4_invalid_Registration_PasswordValidation(self):
        self.log.info("test_t4invalidRegistrationPasswordValidation started")
        self.rp.clickregisterButtonLogin()
        self.rp.register("amitmech89@gmail.com", "test")
        time.sleep(1)
        register_success_result = self.rp.successRegisterPageTitle()
        if register_success_result == True:
            assert False


    def test_t6_invalid_Registration_EmailValidation(self):
        self.log.info("test_t5invalidRegistrationEmailValidation started")
        self.rp.clickregisterButtonLogin()
        register_page_title_result = self.rp.verifyregisterPageTitle()
        self.ts.mark(register_page_title_result, "Registration Page Verification")
        self.rp.register("amitmech89", "test")
        time.sleep(1)
        result = self.rp.invalidEmail()
        self.ts.markFinal("test_t6_invalid_Registration_EmailValidation",result, "invalid Email message Verification")

    def test_t7_invalid_Registration_both_password_field_blank(self):
        self.log.info("test_t5invalidRegistrationEmailValidation started")
        self.rp.clickregisterButtonLogin()
        register_page_title_result = self.rp.verifyregisterPageTitle()
        self.ts.mark(register_page_title_result, "Registration Page Verification")
        self.rp.register("amitmech89@test.com", "")
        time.sleep(1)
        result = self.rp.fillAllDetail()
        self.ts.markFinal("test_t7_invalid_Registration_password_field_blank",result, "Fill All details message Verification")

    def test_t8_invalid_Registration_confirm_password_field_blank(self):
        self.log.info("test_t5invalidRegistrationEmailValidation started")
        self.rp.clickregisterButtonLogin()
        register_page_title_result = self.rp.verifyregisterPageTitle()
        self.ts.mark(register_page_title_result, "Registration Page Verification")
        self.rp.registerWithConfirmPasswordBlank("amit@test.com","Dream@123")
        result = self.rp.confirmPasswordBlank()
        self.ts.markFinal("test_t8_invalid_Registration_confirm_password_field_blank",result, "Confirm password error message Verification")

    def test_t5_invalid_Registration_blank_values(self):
        self.log.info("test_t5invalidRegistrationEmailValidation started")
        self.rp.clickregisterButtonLogin()
        register_page_title_result = self.rp.verifyregisterPageTitle()
        self.ts.mark(register_page_title_result, "Registration Page Verification")
        self.rp.register_blank_values()
        time.sleep(1)
        register_success_result = self.rp.successRegisterPageTitle()
        self.ts.markFinal("test_t5_invalid_Registration_blank_values", register_success_result, "blank values Error message verification")

    def test_t5_1_password_hint_meesage(self):
        self.log.info("test_t5_1_password_hint_meesage started")
        self.rp.clickregisterButtonLogin()
        register_page_title_result = self.rp.verifyregisterPageTitle()
        self.ts.mark(register_page_title_result, "Registration Page Verification")
        self.rp.hintbuttonclick()
        time.sleep(1)
        self.rp.hintbuttonclick()
        tooltip_content_result = self.rp.tooltipcontent()
        self.ts.markFinal("test_t5_1_password_hint_meesage started", tooltip_content_result, "hint pop up dismiss verification")
