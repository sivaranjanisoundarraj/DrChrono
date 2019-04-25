import unittest
import os
from selenium import webdriver
import HtmlTestRunner
from web_ui_testcases.environmentSetup import *
from main.locators import *
from main.pages import *


class ApintEditPatient(object):
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

        "Click Month Tab"
        objcalendarApp.clickMonthTab("month")

        "select Appointment"
        objcalendarApp.selectappointment()

        "Click Edit a patient"
        objcalendarApp.clickEditPatient("patient")

        "click save button"
        objcalendarApp.clickSaveButton("ok")

        "Click Month Tab"
        objcalendarApp.clickMonthTab("month")


class TestApintEditPatient(ApintEditPatient, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ApintEditPatient, cls).setUpClass()


class ApintEditDate(object):
    """
    Verify user is able to edit already scheduled appointment -- edit date
    """

    def testApintEditDate(self):
        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objcalendarApp = CalendarAppointment(self.driver)

        "Click Month Tab"
        objcalendarApp.clickMonthTab("month")

        "select Appointment"
        objcalendarApp.selectappointment()

        "Click Edit a patient"
        objcalendarApp.clickEditPatient("date")

        "click save button"
        objcalendarApp.clickSaveButton("ok")

        "Click Month Tab"
        objcalendarApp.clickMonthTab("month")


class TestApintEditDate(ApintEditDate, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ApintEditDate, cls).setUpClass()


class ApintEditColor(object):
    """
    Verify user is able to edit already scheduled appointment -- edit color
    """

    def testApintEditColor(self):
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

        "Click Edit a patient"
        objcalendarApp.clickEditDetails("color")

        "click save button"
        objcalendarApp.clickSaveButton("ok")

        "Click Month Tab"
        objcalendarApp.clickMonthTab("month")


class TestApintEditColor(ApintEditColor, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ApintEditColor, cls).setUpClass()


class ApintEditDuration(object):
    """
    Verify user is able to edit already scheduled appointment -- edit duration
    """

    def testApintEditDuration(self):
        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objcalendarApp = CalendarAppointment(self.driver)

        "Click Month Tab"
        objcalendarApp.clickMonthTab("month")

        "Select the appointment"
        objcalendarApp.selectappointment()

        "Click Edit a patient"
        objcalendarApp.clickEditDetails("time")

        "click save button"
        objcalendarApp.clickSaveButton("ok")

        "Click Month Tab"
        objcalendarApp.clickMonthTab("month")


class TestApintEditDuration(ApintEditDuration, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ApintEditDuration, cls).setUpClass()


class ApintSelectMonth(object):
    """
    Verify calendar view - Monthly (for current, past & future date)
    """

    def testApintSelectMonth(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objcalendarApp = CalendarAppointment(self.driver)

        "Click Month Tab"
        objcalendarApp.clickEventbutton()

        "select Appointment"
        objcalendarApp.selectPatientName()

        "click save button"
        objcalendarApp.clickSaveButton("")

        "Verify Appointment Event"
        objcalendarApp.verifyAppointmentEvent()

        "select on the future date,month year"
        objcalendarApp.clickMonthTab("month")

        "select on the past date,month year"
        objcalendarApp.clickScreen("past")

        objcalendarApp.clickeventbutton()

        "click the Today event"
        objcalendarApp.selectPatientName()

        "Click save button"
        objcalendarApp.clickSaveButton("ok")

        "Verify Appointment Event"
        objcalendarApp.verifyAppointmentEvent()

        "Select on the future date,month year"
        objcalendarApp.clickMonthTab("month")

        "Select on the past date,month year"
        objcalendarApp.clickScreen("fur")

        objcalendarApp.clickeventbutton()

        "Click the Today event"
        objcalendarApp.selectPatientName()

        "Click save button"
        objcalendarApp.clickSaveButton("")

        "Verify Future Appointment "
        objcalendarApp.verifyAppointmentEvent()


class TestApintSelectMonth(ApintSelectMonth, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ApintSelectMonth, cls).setUpClass()


class ApintSelectDaily(object):
    """
    Verify calendar view - Daily (for current, past & future date)
    """

    def testApintSelectDaily(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objcalendarApp = CalendarAppointment(self.driver)

        "Click Month Tab"
        objcalendarApp.clickMonthTab("daily")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "select Appointment"
        objcalendarApp.selectPatientName()

        "click save button"
        objcalendarApp.clickSaveButton("")

        "Verify Appointment Event"
        objcalendarApp.verifyAppointmentEvent()

        "select on the past date,month year"
        objcalendarApp.clickMonthTab("daily")

        "select on the past date,month year"
        objcalendarApp.clickScreen("past")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "click the Today event"
        objcalendarApp.selectPatientName()

        "Click save button"
        objcalendarApp.clickSaveButton("ok")

        "Verify Appointment Event"
        objcalendarApp.verifyAppointmentEvent()

        "Select on the future date,month year"
        objcalendarApp.clickMonthTab("daily")

        "Select on the past date,month year"
        objcalendarApp.clickScreen("fur")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "Click the Today event"
        objcalendarApp.selectPatientName()

        "Click save button"
        objcalendarApp.clickSaveButton("")

        "Verify Future Appointment "
        objcalendarApp.verifyAppointmentEvent()


class TestApintSelectDaily(ApintSelectDaily, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ApintSelectDaily, cls).setUpClass()


class ApintSelectWeekly(object):
    """
    Verify calendar view - weekly (for current, past & future date)
    """

    def testAppoSelectWeekly(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objcalendarApp = CalendarAppointment(self.driver)

        "Click Month Tab"
        objcalendarApp.clickMonthTab("weekly")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "select Appointment"
        objcalendarApp.selectPatientName()

        "click save button"
        objcalendarApp.clickSaveButton("")

        "Verify Appointment Event"
        objcalendarApp.verifyAppointmentEvent()

        "select on the past date,month year"
        objcalendarApp.clickMonthTab("weekly")

        "select on the past date,month year"
        objcalendarApp.clickScreen("past")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "click the Today event"
        objcalendarApp.selectPatientName()

        "Click save button"
        objcalendarApp.clickSaveButton("ok")

        "Verify Appointment Event"
        objcalendarApp.verifyAppointmentEvent()

        "Select on the future date,month year"
        objcalendarApp.clickMonthTab("weekly")

        "Select on the past date,month year"
        objcalendarApp.clickScreen("fur")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "Click the Today event"
        objcalendarApp.selectPatientName()

        "Click save button"
        objcalendarApp.clickSaveButton("")

        "Verify Future Appointment "
        objcalendarApp.verifyAppointmentEvent()


class TestAppoSelectWeekly(ApintSelectWeekly, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ApintSelectWeekly, cls).setUpClass()


class ApintSelectExamRooms(object):
    """
    Verify calendar view - Exam Rooms (for current, past & future date)
    """

    def testApintSelectExamRooms(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objcalendarApp = CalendarAppointment(self.driver)

        "Click Month Tab"
        objcalendarApp.clickMonthTab("examRooms")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "select Appointment"
        objcalendarApp.selectPatientName()

        "click save button"
        objcalendarApp.clickSaveButton("")

        "Verify Appointment Event"
        objcalendarApp.verifyAppointmentEvent()

        "select on the past date,month year"
        objcalendarApp.clickMonthTab("examRooms")

        "select on the past date,month year"
        objcalendarApp.clickScreen("past")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "click the Today event"
        objcalendarApp.selectPatientName()

        "Click save button"
        objcalendarApp.clickSaveButton("ok")

        "Verify Appointment Event"
        objcalendarApp.verifyAppointmentEvent()

        "Select on the future date,month year"
        objcalendarApp.clickMonthTab("examrooms")

        "Select on the past date,month year"
        objcalendarApp.clickScreen("fur")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "Click the Today event"
        objcalendarApp.selectPatientName()

        "Click save button"
        objcalendarApp.clickSaveButton("")

        "Verify Future Appointment "
        self.assertEqual(objcalendarApp.verifyAppointmentEvent())


class TestApintSelectExamRooms(ApintSelectExamRooms, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ApintSelectExamRooms, cls).setUpClass()


class ApintSelectDoctors(object):
    """
    Verify calendar view - Doctor (for current, past & future date)
    """

    def testApintSelectDoctors(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objcalendarApp = CalendarAppointment(self.driver)

        "Click Month Tab"
        objcalendarApp.clickMonthTab("Doctor")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "select Appointment"
        objcalendarApp.selectPatientName()

        "click save button"
        objcalendarApp.clickSaveButton("")

        "Verify Appointment Event"
        objcalendarApp.verifyAppointmentEvent("daily")

        "select on the past date,month year"
        objcalendarApp.clickMonthTab("Doctor")

        "select on the past date,month year"
        objcalendarApp.clickScreen("past")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "click the Today event"
        objcalendarApp.selectPatientName()

        "Click save button"
        objcalendarApp.clickSaveButton("ok")

        "Verify Appointment Event"
        objcalendarApp.verifyAppointmentEvent("daily")

        "Select on the future date,month year"
        objcalendarApp.clickMonthTab("Doctor")

        "Select on the past date,month year"
        objcalendarApp.clickScreen("fur")

        "Click the event button"
        objcalendarApp.clickeventbutton()

        "Click the Today event"
        objcalendarApp.selectPatientName()

        "Click save button"
        objcalendarApp.clickSaveButton("")

        "Verify Future Appointment "
        self.assertEqual(objcalendarApp.verifyAppointmentEvent("daily"), "Verify the appointment")


class TestAppoSelectDoctors(ApintSelectDoctors, TestBase):
    """
     This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ApintSelectDoctors, cls).setUpClass()


class ApintFilterOffice(object):
    """
    Verify print appointments - filter by office, doctor, date range
    """

    def testApintFilterOffice(self):

        "Creating an object for LoginPage"
        objLoginPage = LoginPage(self.driver)

        "Login To Dr.Chrono Application"
        objLoginPage.login()

        "Creating an object for ScheduleAppointmentEvent"
        objcalendarApp = CalendarAppointment(self.driver)

        "Click Schedule Menu Tab"
        objcalendarApp.clickScheduleMenu()

        "click the print button"
        objcalendarApp.clickPrintButton()

        "click office Filter"
        objcalendarApp.clickOfficeFilter()

        "Select Doctors"
        objcalendarApp.selectDoctors()

        "click to Update Filter"
        objcalendarApp.selectDisplay()


class TestApintFilterOffice(ApintFilterOffice, TestBase):
    """
    This method is inheritance for Base class
    """

    @classmethod
    def setUpClass(cls):
        super(ApintFilterOffice, cls).setUpClass()


class UserScheduleAppointment(object):
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
    Verify user is able to schedule appointment by clicking '+Event'
    and searching existing  patient from list with all fields selection
    """

    @classmethod
    def setUpClass(cls):
        super(UserScheduleAppointment, cls).setUpClass()
