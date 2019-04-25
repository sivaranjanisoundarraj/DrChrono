import unittest
import os
from selenium import webdriver
import HtmlTestRunner
from web_ui_testcases.environmentSetup import *
from main.locators import *
from main.pages import *


class AddnewPatientUsingNewPatientButton(object):
    """
    Verify user is able to edit already scheduled appointment -- edit patient
    """

    def testApintEditPatient(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objcalendarApp = CalendarAppointment(self.driver)

        objcalendarApp.clickScheduleMenu()

        objcalendarApp.clickEventbutton()

        objcalendarApp.clickNewPatientBut()


class TestApintEditPatient(AddnewPatientUsingNewPatientButton, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(AddnewPatientUsingNewPatientButton, cls).setUpClass()
