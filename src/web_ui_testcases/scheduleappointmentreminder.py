import os
import sys
from web_ui_testcases.environmentSetup import TestBase
from main.pages import *
from main.locators import *


class ScheduleAppointmentRemider(object):
    """
    Verify user is able to view active reminders
    """

    def testScheduleappointmentViewactiveRemider(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        "Navigate To Appointment Schedule Screen"
        objScheduleAppointment.clickEventbutton()

        "Select a Patient"
        objScheduleAppointment.selectPatientName()

        "Enter Additional Appointment Details"
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        "Click View Reminder"
        objScheduleAppointment.clickViewReminder()

        "Click Save Button"
        objScheduleAppointment.clickSaveButton("")

        "Verify Appointment tEvent"
        objScheduleAppointment.verifyAppointmentEvent()


class TestScheduleAppointmentRemider(ScheduleAppointmentRemider, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ScheduleAppointmentRemider, cls).setUpClass()


class ScheduleAppointmentViewProfile(object):
    """
    Verify user is able to schedule appointment using ViewProfile
    """

    def testScheduleAppointmentViewProfile(self):
        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        "Navigate To Appointment Schedule Screen"
        objScheduleAppointment.clickEventbutton()

        "Select a Patient"
        objScheduleAppointment.selectPatientName()

        "Enter Additional Appointment Details"
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        "Add ReminderProfile"
        objScheduleAppointment.addReminderProfile()

        "Click Save Button"
        objScheduleAppointment.clickSaveButton("")

        "Verify Appointment tEvent"
        objScheduleAppointment.verifyAppointmentEvent()


class TestScheduleAppointmentViewProfile(ScheduleAppointmentViewProfile, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ScheduleAppointmentViewProfile, cls).setUpClass()


class ScheduleAppointmentFollowUpDate(object):
    """
    Verify user is able to schedule appointment using Appointment FollowUp Date
    """

    def testScheduleAppointmentFollowUpDate(self):
        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        "Navigate To Appointment Schedule Screen"
        objScheduleAppointment.clickEventbutton()

        "Select a Patient"
        objScheduleAppointment.selectPatientName()

        "Enter Additional Appointment Details"
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        "Click Arrange Follow Up Reminder"
        objScheduleAppointment.clickArrangeFollowupReminder()

        "Click to Save Button"
        objScheduleAppointment.clickSaveButton("")

        "Verify Appointment Event"
        objScheduleAppointment.verifyAppointmentEvent()


class TestScheduleAppointmentFollowUpDate(ScheduleAppointmentFollowUpDate, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ScheduleAppointmentFollowUpDate, cls).setUpClass()


class ScheduleAppointmentRecurring(object):
    """
    Verify user is able to schedule appointment using Appointment FollowUp Date
    """

    def testScheduleAppointmentRecurring(self):
        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        "Navigate To Appointment Schedule Screen"
        objScheduleAppointment.clickEventbutton()

        "Select a Patient"
        objScheduleAppointment.selectPatientName()

        "Enter Additional Appointment Details"
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        "Click Arrange Follow Up Reminder"
        objScheduleAppointment.clickRecurringAppointment()

        "Click to Save Button"
        objScheduleAppointment.clickSaveButton("")

        "Verify Appointment Event"
        objScheduleAppointment.verifyAppointmentEvent()


class TestScheduleAppointmentRecurring(ScheduleAppointmentRecurring, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ScheduleAppointmentRecurring, cls).setUpClass()


class ScheduleappiontmentRecurringNeverEnd(object):
    """
    Verify user is able to schedule recurring appointment  Never End
    """

    def testScheduleappiontmentRecurringNeverEnd(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        "Navigate To Appointment Schedule Screen"
        objScheduleAppointment.clickEventbutton()

        "Select a Patient Name"
        objScheduleAppointment.selectPatientName()

        "Enter Additional  Appointment Details"
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        "Click Recurring ParticularD Day"
        objScheduleAppointment.clickRecurringParticularday()

        "Click SaveButton"
        objScheduleAppointment.clickSaveButton("")

        "Verify Appointment Event"
        objScheduleAppointment.verifyAppointmentEvent()


class TestScheduleappiontmentRecurringNeverEnd(ScheduleappiontmentRecurringNeverEnd, TestBase):
    """
     This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ScheduleappiontmentRecurringNeverEnd, cls).setUpClass()


class appiontmentEditActiveReminder(object):
    """
    Verify user is able to add new Reminders profile selection-Edit reminder
    """

    def testappiontmentEditActiveReminder(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        "Navigate To Appointment Schedule Screen"
        objScheduleAppointment.clickEventbutton()

        "Select a Patient Name"
        objScheduleAppointment.selectPatientName()

        "Enter Additional  Appointment Details"
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        "Click the View Reminder"
        objScheduleAppointment.clickViewReminder()

        "Edit Reminder profile"
        objScheduleAppointment.clickNewReminder()

        "Edit Reminder Details"
        objScheduleAppointment.clickEditReminder()

        "Delete reminder listed below"
        objScheduleAppointment.deleteReminderProfile("")

        "Click SaveButton"
        objScheduleAppointment.clickSaveButton("")

        "Verify Appointment Event"
        objScheduleAppointment.verifyAppointmentEvent()


class TestAppiontmentEditActiveReminder(appiontmentEditActiveReminder, TestBase):
    """
     This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(appiontmentEditActiveReminder, cls).setUpClass()


class appiontmentAddAcitveReminder(object):
    """
    Verify user is able to add new Reminders with profile selection-Add reminder
    """

    def testappiontmentAddAcitveReminder(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objScheduleAppointment = ScheduleAppointmentEvent(self.driver)

        "Navigate To Appointment Schedule Screen"
        objScheduleAppointment.clickEventbutton()

        "Select a Patient Name"
        objScheduleAppointment.selectPatientName()

        "Enter Additional  Appointment Details"
        objScheduleAppointment.enterAdditionalAppointmentDetails()

        "Click the View Reminder"
        objScheduleAppointment.clickViewReminder()

        "Edit Reminder profile"
        objScheduleAppointment.clickNewReminder()

        "Edit Reminder Details"
        objScheduleAppointment.clickEditReminder()

        "Click SaveButton"
        objScheduleAppointment.clickSaveButton("")

        "Verify Appointment Event"
        objScheduleAppointment.verifyAppointmentEvent()


class TestappiontmentAddAcitveReminder(appiontmentAddAcitveReminder, TestBase):
    """
     This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(appiontmentAddAcitveReminder, cls).setUpClass()


class UserScheduleAppointment(object):
    """
    Verify user is able to schedule appointment by clicking '+Event'
    and searching existing  patient from list with all fields selection
    """

    def testUserScheduleAppointment(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objcalendarApp = CalendarAppointment(self.driver)

        "Click Month Tab"
        objcalendarApp.clickMonthTab("month")

        "Select the Appointment"
        objcalendarApp.selectappointment()

        "Enter Additional Appointment details"
        objcalendarApp.enterAdditionalAppointmentDetails()

        "Select a status"
        objcalendarApp.selectStatus()

        "select the profile"
        objcalendarApp.selectProfile()

        "click the exam room"
        objcalendarApp.clickExam()

        "select the  color"
        objcalendarApp.selectColor()

        "click save button"
        objcalendarApp.clickSaveButton("ok")

        "click the Month tab"
        objcalendarApp.clickMonthTab("month")

        "Select the Appointment"
        objcalendarApp.selectappointment()


class TestUserScheduleAppointment(UserScheduleAppointment, TestBase):
    """
     This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(UserScheduleAppointment, cls).setUpClass()
