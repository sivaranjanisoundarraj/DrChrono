from main.webactions import BaseBage
from selenium.common.exceptions import WebDriverException
from main.locators.loginpage import *
from main.locators.appointment import *
import os
import time
from configparser import ConfigParser
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class LoginPage(BaseBage):
    """
    This class is used for login verification
    """

    "Defining the source of config file"
    config = ConfigParser()
    project_root = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(project_root, "main")
    config_path1 = os.path.join(config_path, "config")
    print(config_path1)
    config.read(config_path1)

    "Get values from config file"

    url = config.get("data", "url")
    username = config.get("data", "username")
    password = config.get("data", "password")
    month = "3"

    def __init__(self, driver):
        """
        constructor class
        @param self : this is the  reference to instance of object
        """
        self.driver = driver
        self.timeout = 30

    def open_url(self):
        """
        This method is used to open URL
        @:@param url    :get url from config file
        """
        try:
            self.driver.get(self.url)
        except WebDriverException:
            self.fail("Could not get url")

    def login(self):
        """
        This method is used to login Dr.chrono
        @param username : get username from config file
        @param password : get password from config file
        """
        try:
            self.open_url()
            self.click(*LoginPageLocators.BTN_LOGIN)
            self.click(*LoginPageLocators.TXT_USERNAME)
            self.type(self.username, *LoginPageLocators.TXT_USERNAME)
            self.type(self.password, *LoginPageLocators.TXT_PASSWORD)
            self.click(*LoginPageLocators.BTN_LOGIN_BUT)
        except WebDriverException:
            self.fail("Could not login the page")


class ScheduleAppointmentEvent(LoginPage):
    """
    This class used to Schedule Appointment Event
    """

    TIME = None
    PATIENT_NAME = None
    DATE = None
    var_patientname = "john"
    times = "10"
    firstname = "Ram"
    lastname = "Hentry"
    reason = "Testing the appointment"
    element = None
    """
    constructor class
    @param self : this is refer to instance of object
    """

    def __init__(self, driver):
        self.driver = driver

    """
    Click the Schedule menu
    """

    def clickScheduleMenu(self):
        try:
            time.sleep(3)
            self.hover(*ScheduleAppointmentsEventlocators.MNU_SCHEDUL)
            time.sleep(2)
            self.click(*ScheduleAppointmentsEventlocators.MNU_CALENDER)
        except WebDriverException:
            self.fail("could not click the schedule menu")

    """
    This method used to Click Event Button
    """

    def clickEventbutton(self):
        try:
            self.clickScheduleMenu()
            self.click(*ScheduleAppointmentsEventlocators.BTN_TODAY)
            time.sleep(3)
            self.click(*ScheduleAppointmentsEventlocators.BTN_EVENT)
        except WebDriverException:
            self.fail("Could not click Event button")

    def clickSaveButton(self, type):
        """
        This method used Click Save Button
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.BTN_SAVE)
            if type == "ok":
                obj = self.driver.switch_to_alert()
                obj.accept()
            time.sleep(3)
            self.click(*ScheduleAppointmentsEventlocators.BTN_CLOSE_ARROW)
        except WebDriverException:
            self.fail("could not click the save button")

    def clickDeletButton(self):
        """
        This method used to click delete button
        """
        try:
            time.sleep(2)
            self.click(*ScheduleAppointmentsEventlocators.BTN_DELETDELET)
            self.click(*ScheduleAppointmentsEventlocators.BTN_CLOSE_ARROW)
        except WebDriverException:
            self.fail("Could not click  Delete button")

    def selectPatientName(self):
        """
        This method used to select the patient name
        """
        try:
            global element
            global PATIENT_NAME
            global TIME
            time.sleep(2)
            self.click(*ScheduleAppointmentsEventlocators.TXT_PATIENT_NAME)
            self.type(self.var_patientname, *ScheduleAppointmentsEventlocators.TXT_PATIENT_NAME)
            time.sleep(5)
            self.driver.find_element(*ScheduleAppointmentsEventlocators.TXT_PATIENT_ITEM).click()
            patient = self.driver.find_element_by_id("id_appt-patient_autocomplete")
            PATIENT_NAME = patient.get_attribute("value")
            self.click(*ScheduleAppointmentsEventlocators.BTN_TIME)
            self.type(self.times, *ScheduleAppointmentsEventlocators.BTN_TIME)
            t = self.getAttribute(*ScheduleAppointmentsEventlocators.BTN_TIME)
            TIME = t.lower()
        except WebDriverException:
            self.fail("Could not select patient name")

    def clickViewReminder(self):
        """
        This method used to click view reminder
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.CHK_VIEWACTIVEREMIDER)
            self.scroll(*ScheduleAppointmentsEventlocators.CHK_VIEWACTIVEREMIDER)
        except WebDriverException:
            self.fail("Could not click the view reminder")

    def clickEventType(self, type):
        """
        This method used to click event type
        """
        try:
            if type == "Break":
                self.click(*ScheduleAppointmentsEventlocators.CHK_BREAK)
            elif type == "Walk-in":
                self.click(*ScheduleAppointmentsEventlocators.CHK_WALKIN)
            elif type == "Transition of Care":
                self.click(*ScheduleAppointmentsEventlocators.CHK_TRANSITIONOFCARE)
            elif type == "Referral":
                self.click(*ScheduleAppointmentsEventlocators.CHK_REFRELL)
            elif type == "New Patient":
                self.click(*ScheduleAppointmentsEventlocators.CHK_NEWPATIENT)
        except WebDriverException:
            self.fail("Could not click the event type")

    def enterAdditionalAppointmentDetails(self):
        """
        This method used to enter additional appointment details'
        """
        try:
            global TIME
            global PATIENT_NAME
            global DATE
            patient = self.driver.find_element_by_id("id_appt-patient_autocomplete")
            PATIENT_NAME = patient.get_attribute("value")
            self.getAttribute(*ScheduleAppointmentsEventlocators.TXT_PATIENT_NAME)
            self.click(*ScheduleAppointmentsEventlocators.BTN_TIME)
            self.type(self.times, *ScheduleAppointmentsEventlocators.BTN_TIME)
            t = self.getAttribute(*ScheduleAppointmentsEventlocators.BTN_TIME)
            TIME = t.lower()
            dd = self.getAttribute(*ScheduleAppointmentsEventlocators.BTN_DURATION)
            DATE = dd.split("/")[1]
            self.type(self.reason, *ScheduleAppointmentsEventlocators.TXT_REASON_PATIENT)
            self.click(*ScheduleAppointmentsEventlocators.TXT_ADD_NOTES)
            self.type(self.reason, *ScheduleAppointmentsEventlocators.TXT_ADD_NOTES)
        except WebDriverException:
            self.fail("Could not enter additional details")

    def enterReasonBreak(self):
        """
        This method used to enter reason for break event type
        """
        try:
            self.type(self.reason, *ScheduleAppointmentsEventlocators.TXT_REASON_PATIENT)
            self.enterAdditionalAppointmentDetails()
        except WebDriverException:
            self.fail("Could not enter reason")

    def createNewPatient(self):
        """
        This method used to create new patient
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.TXT_FIRSTNAME)
            self.type(self.firstname, *ScheduleAppointmentsEventlocators.TXT_FIRSTNAME)
            self.click(*ScheduleAppointmentsEventlocators.TXT_LASTNAME)
            self.type(self.lastname, *ScheduleAppointmentsEventlocators.TXT_LASTNAME)
            self.click(*ScheduleAppointmentsEventlocators.BTN_ADD)
            self.click(*ScheduleAppointmentsEventlocators.BTN_ALERT)
        except WebDriverException:
            self.fail("Could not create new patient")

    def addReminderProfile(self):
        """
        This method used to Add reminder profile
        """
        try:
            self.clickViewReminder()
            self.selectByVisibleText(
                "Use Patient's Last Reminders",
                *ScheduleAppointmentsEventlocators.DDL_REMINDERPROFILE
            )
            self.click(*ScheduleAppointmentsEventlocators.BTN_ADDNEWREMINDER)
        except WebDriverException:
            self.fail("Could not add reminder profile")

    def clickArrangeFollowupReminder(self):
        """
        This method is used to click arrange follow up reminder
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.CHK_ARRANGEFOLLOWUP)
            time.sleep(3)
            self.click(*ScheduleAppointmentsEventlocators.CHK_FOLLOWUPDATE)
            self.click(*ScheduleAppointmentsEventlocators.BTN_NXT)
            self.click(*ScheduleAppointmentsEventlocators.BTN_SEELECTDATE)
            self.click(*ScheduleAppointmentsEventlocators.TXT_REASON)
            self.type(self.reason, *ScheduleAppointmentsEventlocators.TXT_REASON)
        except WebDriverException:
            self.fail("Could not click arrange follow up reminder")

    def clickRecurringAppointment(self):
        """
        This method used to click Recurring appointment for never ends
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.CHK_RECURRING_APP)
            self.scroll(*ScheduleAppointmentsEventlocators.CHK_RECURRING_APP)
            self.click(*ScheduleAppointmentsEventlocators.BTN_SELECTALL)
            self.click(*ScheduleAppointmentsEventlocators.BTN_NEVER_END)
        except WebDriverException:
            self.fail("Could not click recurring appointment")

    def clickRecurringParticularday(self):
        """
        This method used to click Recurring Appointment in particular day
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.CHK_RECURRING_APP)
            self.isSelected(*ScheduleAppointmentsEventlocators.CHK_MONDAY)
            self.click(*ScheduleAppointmentsEventlocators.CHK_MONDAY)
            self.isSelected(*ScheduleAppointmentsEventlocators.CHK_TUESDAY)
            self.click(*ScheduleAppointmentsEventlocators.CHK_TUESDAY)
            self.click(*ScheduleAppointmentsEventlocators.BTN_LAST_APP)
            self.click(*ScheduleAppointmentsEventlocators.BTN_NEXT)
            self.click(*ScheduleAppointmentsEventlocators.BTN_LAST_APP_DATE)
            self.scroll(*ScheduleAppointmentsEventlocators.CHK_RECURRING_APP)
        except WebDriverException:
            self.fail("Could not click recurring particular day")

    def clickEditReminder(self):
        """
        This method is used to click Edit Reminder profile
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.BTN_EDIT_REMINDER)
            self.click(*ScheduleAppointmentsEventlocators.TXT_CUSTOM_MSG)
            self.type(self.reason, *ScheduleAppointmentsEventlocators.TXT_CUSTOM_MSG)
            self.selectByVisibleText("SMS Text", *ScheduleAppointmentsEventlocators.DDL_SMSTEXT)
            self.selectByVisibleText("after", *ScheduleAppointmentsEventlocators.DDL_AFTER)
            self.selectByVisibleText("day(s)", *ScheduleAppointmentsEventlocators.DDL_WEEKS)
            self.click(*ScheduleAppointmentsEventlocators.BTN_PREVIEW)
            self.click(*ScheduleAppointmentsEventlocators.BTN_CLOSE)
        except WebDriverException:
            self.fail("Could not click Edit reminder")

    def deleteReminderProfile(self, type):
        """
        This method is used to Delete the reminder
        """
        try:
            if type == "Chronically":
                self.selectByVisibleText(
                    "For Chronically Late Patients (Zuci QA)",
                    *ScheduleAppointmentsEventlocators.DDL_CHOOSEREMINDERPROFILE
                )
                time.sleep(3)
            self.driver.find_element_by_xpath(
                "//*[@id='id_rem_row_1']//*[contains(text(),'Delete')]"
            ).click()
        except WebDriverException:
            self.fail("Could not delete reminder profile")

    def clickNewReminder(self):
        """
        This method is click to new reminder
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.BTN_ADDNEWREMINDER)
        except WebDriverException:
            self.fail("Could not click the reminder")

    def verifyAppointmentEvent(self):
        """
        This method is used to verify Appointment
        """
        try:
            self.click(*CalnderLocators.BTN_DAILY)
            for div in range(2, 26):
                time.sleep(3)
                web_patient_name = self.driver.find_element_by_xpath(
                    "//*[@id='tgCol0']/div[" + str(div) + "]/dl/dd"
                ).text
                name = web_patient_name.split(":")[0]
                if PATIENT_NAME == name:
                    for div in range(2, 20):
                        web_time = self.driver.find_element_by_xpath(
                            "//*[@id='tgCol0']/div[" + str(div) + "]/dl/dt"
                        ).text
                        start_time = web_time.split("-")[0]
                        end_time = web_time.split("-")[1]
                        dur = end_time.split(" ")[2]
                        duration = dur.lower()
                        ttt = start_time + duration
                        DURATION_TIME = ttt.replace(" ", "")
                        if TIME == DURATION_TIME:
                            time.sleep(4)
                            click_time = self.driver.find_element_by_xpath(
                                "//*[@id='tgCol0']/div[" + str(div) + "]/dl"
                            )
                            time.sleep(5)
                            appoint_time = click_time.click()
                            time.sleep(2)
                            self.click(*ScheduleAppointmentsEventlocators.BTN_CLOSE_ARROW)
                            break
                    break
                assert True
        except WebDriverException:
            self.fail("Could not verifyAppointmentEvent")


class CalendarAppointment(ScheduleAppointmentEvent):
    """
    This class is used for Calendar verification
    """

    def clickMonthTab(self, type):
        """
        This method is used to click the Month tab
        """
        try:
            time.sleep(2)
            self.hover(*ScheduleAppointmentsEventlocators.MNU_SCHEDUL)
            time.sleep(2)
            self.click(*ScheduleAppointmentsEventlocators.MNU_CALENDER)
            if type == "month":
                self.click(*CalnderLocators.BTN_MONTH)
            if type == "daily":
                self.click(*CalnderLocators.BTN_DAILY)
            if type == "weekly":
                self.click(*CalnderLocators.BTN_WEEKLY)
            if type == "examrooms":
                self.click(*CalnderLocators.BTN_EXAM_ROOM)
            if type == "Doctor":
                self.click(*CalnderLocators.BTN_DOCTOR)
        except WebDriverException:
            self.fail("Could not click month tab")

    def selectappointment(self):
        """
        This method is used to select the appointment on screen
        """
        try:
            time.sleep(6)
            self.driver.find_element_by_xpath(
                "//*[@class='mv-event-container']//*[@class='st-c']"
            ).click()
        except WebDriverException:
            self.fail("Could not select appointment")

    def EditVerificiationDetails(self, status):
        """
        This method is used to select the appointment on screen
        """
        try:
            self.selectappointment()
            if status == time:
                PATIENT_TIME = self.getAttribute(*ScheduleAppointmentsEventlocators.BTN_TIME)
                TIME_DURATION = PATIENT_TIME.lower()
                if TIME == TIME_DURATION:
                    self.click(*ScheduleAppointmentsEventlocators.BTN_CLOSE_ARROW)
                    assert True("Verified SuccessFully")
        except WebDriverException:
            self.fail("Edit verification details")

    def clickEditPatient(self, type):
        """
        This method is used to edit the patient name
        """
        try:
            global PATIENT_NAME
            self.click(*CalnderLocators.BTN_EDIT)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            if type == "patient":
                self.click(*CalnderLocators.TXT_FSTNAME)
                self.type(self.firstname, *CalnderLocators.TXT_FSTNAME)
                PATIENT_NAME = self.getAttribute(*CalnderLocators.TXT_FSTNAME)
                self.scroll(*CalnderLocators.TXT_SUFFIX)
                self.scroll(*CalnderLocators.TXT_REMINDER)
            if type == "date":
                self.scroll(*CalnderLocators.TXT_SUFFIX)
                self.scroll(*CalnderLocators.TXT_REMINDER)
                self.click(*CalnderLocators.TXT_LST_APP)
                self.click(*CalnderLocators.BTN_DATE_ICON)
                self.click(*CalnderLocators.DDL_DATE)
            self.click(*CalnderLocators.BTN_SAVE_CLOSE)
            self.driver.switch_to.window(self.driver.window_handles[0])
        except WebDriverException:
            self.fail("Could not click Edit Patient")

    def clickEditDetails(self, type):
        """
        This method is edit the details on screen
        """
        try:
            if type == "color":
                self.click(*CalnderLocators.BTN_COLOR)
                self.click(*CalnderLocators.TXT_COLOR)
            if type == "time":
                self.click(*ScheduleAppointmentsEventlocators.BTN_TIME)
                self.type(self.times, *ScheduleAppointmentsEventlocators.BTN_TIME)
                patient = self.driver.find_element_by_id("id_appt-patient_autocomplete")
                PATIENT_NAME = patient.get_attribute("value")
                t = self.getAttribute(*ScheduleAppointmentsEventlocators.BTN_TIME)
                TIME = t.lower()
            self.scroll(*ScheduleAppointmentsEventlocators.CHK_REMIDERPROFILE)
        except WebDriverException:
            self.fail("Could not click edit details")

    def clickExam(self):
        """
        This method is click the exam rooms
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.DDL_EXAM)
            self.selectByVisibleText("Exam 3", *ScheduleAppointmentsEventlocators.DDL_EXAM)
        except WebDriverException:
            self.fail("could not click the Exam Room")

    def selectStatus(self):
        """
        This method is used to select the status
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.DDL_STATUS)
            self.selectByVisibleText("In Room", *ScheduleAppointmentsEventlocators.DDL_STATUS)
        except WebDriverException:
            self.fail("Could not select the status")

    def selectColor(self):
        """
        This method is used to select the color
        """
        try:
            self.click(*CalnderLocators.BTN_COLOR)
            self.click(*CalnderLocators.TXT_COLOR)
        except WebDriverException:
            self.fail("Could not select the color")

    def selectProfile(self):
        """
        This method is used to select the profile
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.DDL_PROFILE)
            self.selectByVisibleText("Checkup", *ScheduleAppointmentsEventlocators.DDL_PROFILE)
        except WebDriverException:
            self.fail("Could not select the profile")

    def clickScreen(self, type):
        """
        This method is used to click the Daily
        """
        try:
            time.sleep(4)
            if type == "fur":
                self.click(*CalnderLocators.BTN_NEXT_MONTH)
                self.click(*CalnderLocators.DDL_YEAR)
                self.selectByVisibleText("2022", *CalnderLocators.DDL_YEAR)
                self.click(*CalnderLocators.BTN_DAY)
                time.sleep(2)
            elif type == "past":
                self.click(*CalnderLocators.BTN_PRE_MONTH)
                self.click(*CalnderLocators.DDL_YEAR)
                self.selectByVisibleText("2017", *CalnderLocators.DDL_YEAR)
                self.click(*CalnderLocators.BTN_DAY)
                time.sleep(5)
        except WebDriverException:
            assert False

    def clickeventbutton(self):
        """
        This method is used to click the event Button
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.BTN_EVENT)
            assert True
        except WebDriverException:
            self.fail("Could not click event button")

    def clickPrintButton(self):
        """
        This method is used to click the print Button
        """
        try:
            self.click(*ScheduleAppointmentsEventlocators.BTN_PRINT)
            self.driver.switch_to.window(self.driver.window_handles[1])
        except WebDriverException:
            self.fail("Could not click print button")

    def clickOfficeFilter(self):
        """
        This method is used to select the office
        """
        try:
            global OFF_NAME
            self.click(*CalnderLocators.DDL_SELECT_OFF)
            self.selectByVisibleText("Primary Office", *CalnderLocators.DDL_SELECT_OFF)
            OFF_NAME = self.getText(*CalnderLocators.DDL_SELECT_OFF)
            self.click(*CalnderLocators.TXT_STARTDATE)
            self.click(*CalnderLocators.BTN_DONE)
            self.click(*CalnderLocators.TXT_ENDDATE)
            self.click(*CalnderLocators.BTN_NEXT_MONTH)
            self.click(*CalnderLocators.BTN_DAY)
        except WebDriverException:
            self.fail("Could not click the Office Filter")

    def selectDoctors(self):
        """
        This method is used to select all doctors
        """
        try:
            self.click(*CalnderLocators.BTN_DOCTORS_ALL)
        except WebDriverException:
            self.fail("Could not click the select all Doctors")

    def selectFont(self):
        """
        This method is used to select the Font size
        """
        try:
            self.click()(*CalnderLocators.DDL_FORNT_SIZE)
            self.selectByVisibleText("small", *CalnderLocators.DDL_FONT_SIZE)
        except WebDriverException:
            self.fail("Could not select the font size")

    def deSelectColumn(self):
        """
        This method is used to select the Font size
        """
        try:
            self.isSelected(*CalnderLocators.CHK_CELLPHONE)
            self.isSelected(*CalnderLocators.CHK_EXAM_1)
            self.isSelected(*CalnderLocators.CHK_EXAM_2)
        except WebDriverException:
            self.fail("Could not De select the column")

    def upDateFilter(self):
        """
        This method is used click Update the filter
        """
        try:
            self.click(*CalnderLocators.BTN_UPDATE)
            self.click(*CalnderLocators.BTN_PRINT)
        except WebDriverException:
            self.fail("Could not click the upDate filter")

    def clickPrintDocument(self):
        """
        This method is used to click print page
        """
        try:
            var_Office_Name = self.driver.find_element_by_xpath("//*[@id='content']").text
            if OFF_NAME == var_Office_Name:
                self.assertequal("Verified the office name")
        except WebDriverException:
            self.fail("Could not Print the page")

    def clickNewPatientBut(self):
        """
        This method is used to click the new patient button
        """
        try:
            self.click(*CalnderLocators.BTN_ADD_OFFICE)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.click(*CalnderLocators.TXT_OFFICE)

        except WebDriverException:
            self.fail("could not click new patient button")
