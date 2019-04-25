import unittest
from selenium import webdriver
import os
from main.locators import *
from main.pages import *
import HtmlTestRunner
from web_ui_testcases.environmentSetup import TestBase

"""
Test case for login page
"""


class ValidateLogin(object):

    "Verify user is able to SignUp"

    def testValidCredentials(self):
        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()


"""
This method is inheritance of  TestBase class- Testcase for Login verification
"""


class TestLogin(ValidateLogin, TestBase):
    @classmethod
    def setUpClass(cls):
        super(ValidateLogin, cls).setUpClass()
