import unittest
from selenium import webdriver
from web_ui_testcases.environmentSetup import TestBase
from main.pages import *
from main.locators import *
import HtmlTestRunner
"""
  Verify user is able to schedule appointment by Event
"""


class ScheduleAppointmentEventType(object):

    def testScheduleappointmentType(self):

        'Creating an object for LoginPage'
        objLoginPage = LoginPage(self.driver)

        'Login To Dr.Chrono Application'
        objLoginPage.login()

        'Creating an object for ScheduleAppointmentEvent'
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        'Navigate To Appointment Schedule Screen'
        objScheduleAppointment.clickEventbutton()

        'Select a Patient'
        objScheduleAppointment.selectPatientName()

        'Enter Additional Appointment Details'
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        'Click Save'
        objScheduleAppointment.clickSaveButton('')

        'Verified the Appointment'
        objScheduleAppointment.verifyAppointmentEvent()


"""
 This method is inheritance for TestBase class -Test case
"""


class TestScheduleAppointmentEvent(ScheduleAppointmentEventType, TestBase):
    @classmethod
    def setUpClass(cls):
        super(ScheduleAppointmentEventType, cls).setUpClass()


"""
Verify user is able to schedule appointment using Event with Break type
"""


class ScheduleAppointmentBreak(object):

    def testScheduleappointmentBreak(self):

        'Creating an object for LoginPage'
        objLoginPage = LoginPage(self.driver)

        'Login To Dr.Chrono Application'
        objLoginPage.login()

        'Creating an object for ScheduleAppointmentEvent'
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        'Navigate To Appointment Schedule Screen'
        objScheduleAppointment.clickEventbutton()

        'Click Event Type'
        objScheduleAppointment.clickEventType('Break')

        'Select a Patient'
        objScheduleAppointment.selectPatientName()

        'Enter Additional Appointment Details'
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        'Click Save'
        objScheduleAppointment.clickSaveButton('')

        'Verify Appointment Event'
        objScheduleAppointment.verifyAppointmentEvent()


"""
 This method is inheritance for TestBase class - Test case
"""

'Test case for schedule appointment with break type '


class TestScheduleAppointmentBreak(ScheduleAppointmentBreak, TestBase):
    @classmethod
    def setUpClass(cls):
        super(ScheduleAppointmentBreak, cls).setUpClass()


"""
 Verify user is able to schedule appointment by clicking Event of type Referral
"""


class ScheduleAppointmentReferral(object):
    def testScheduleappointmentReferral(self):

        'Creating an object for LoginPage'
        objLoginPage = LoginPage(self.driver)

        'Login To Dr.Chrono Application'
        objLoginPage.login()

        'Creating an object for ScheduleAppointmentEvent'
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        'Navigate To Appointment Schedule Screen'
        objScheduleAppointment.clickEventbutton()

        'Click Event Type'
        objScheduleAppointment.clickEventType('Referral')

        'Select a Patient Name'
        objScheduleAppointment.selectPatientName()

        'Enter Additional Appointment Details'
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        'Click Save'
        objScheduleAppointment.clickSaveButton('')

        'Verify Appointment Event'
        objScheduleAppointment.verifyAppointmentEvent()


"""
 This method is inheritance for TestBase class
"""
'Test case - schedule appointment by event with referral type'


class TestScheduleAppointmentReferral(ScheduleAppointmentReferral, TestBase):
    @classmethod
    def setUpClass(cls):
        super(ScheduleAppointmentReferral, cls).setUpClass()


"""
Verify user can schedule appointment by event with Transition of care type
"""


class ScheduleAppointmentTransitionofcare(object):

    def testScheduleappointmentTranisitionofcare(self):

        'Creating an object for LoginPage'
        objLoginPage = LoginPage(self.driver)

        'Login To Dr.Chrono Application'
        objLoginPage.login()

        'Creating an object for ScheduleAppointmentEvent'
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        'Click Event Button'
        objScheduleAppointment.clickEventbutton()

        'Click Event Type'
        objScheduleAppointment.clickEventType('Transition of Care')

        'Select a Patient Name'
        objScheduleAppointment.selectPatientName()

        'Enter Additional AppiontmentDetails'
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        'Click Save'
        objScheduleAppointment.clickSaveButton('')

        'Verify Appointment Event'
        objScheduleAppointment.verifyAppointmentEvent()


"""
 This method is inheritance for TestBase class
"""

'Test case - schedule appointment by event with transitionOfCare type'


class TestScheduleAppointmentTransitionofcare(ScheduleAppointmentTransitionofcare, TestBase):
    @classmethod
    def setUpClass(cls):
        super(ScheduleAppointmentTransitionofcare, cls).setUpClass()


"""
Verify user is able to schedule appointment by Event with walk-in type
"""


class ScheduleappiontmentWalkin(object):

    def testScheduleappiontmentWalkin(self):

        'Creating an object for LoginPage'
        objLoginPage = LoginPage(self.driver)

        'Login To Dr.Chrono Application'
        objLoginPage.login()

        'Creating an object for ScheduleAppointmentEvent'
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        'Navigate To Appointment Schedule Screen'
        objScheduleAppointment.clickEventbutton()

        'Click Event Type'
        objScheduleAppointment.clickEventType('Walk-in')

        'Select a Patient Name'
        objScheduleAppointment.selectPatientName()

        'Enter Additional  Appointment Details'
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        'Click SaveButton'
        objScheduleAppointment.clickSaveButton('')

        'Verify Appointment tEvent'
        objScheduleAppointment.verifyAppointmentEvent()


"""
 This method is inheritance for Base class
"""

'Test case - schedule appointment event with Walk-in type'


class TestScheduleappiontmentWalkin(ScheduleappiontmentWalkin, TestBase):
    @classmethod
    def setUpClass(cls):
        super(ScheduleappiontmentWalkin, cls).setUpClass()


"""
 This method is inheritance for Base class
""" 
'Testcase - schedule appointment event Patient-in type'


class ScheduleappiontmentNewPatient(object):
    ''
    def testScheduleappiontmentNewPatient(self):

        'Creating an object for LoginPage' 
        objLoginPage = LoginPage(self.driver)

        'Login To Dr.Chrono Application'
        objLoginPage.login()

        'Creating an object for ScheduleAppointmentEvent'
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        'Click Event Button'
        objScheduleAppointment.clickEventbutton()

        'Click Event Type'
        objScheduleAppointment.clickEventType('New Patient')

        'Create a Patient Name'
        objScheduleAppointment.createNewPatient()

        'Enter Additional  Appointment Details'
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        'Click SaveButton'
        objScheduleAppointment.clickSaveButton('')

        'Verify Appointment Event'
        objScheduleAppointment.verifyAppointmentEvent()


"""
 This method is inheritance for Base class
""" 
'Testcase - schedule appointment event with Patient type'


class TestScheduleappiontmentNewPatient(ScheduleappiontmentNewPatient, TestBase):
    @classmethod
    def setUpClass(cls):
        super(ScheduleappiontmentNewPatient, cls).setUpClass()