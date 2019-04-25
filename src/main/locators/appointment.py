from selenium.webdriver.common.by import By


class ScheduleAppointmentsEventlocators(object):
    """
    This class used to Schedule  appointment by  Event -locators
    """

    MNU_SCHEDUL = (By.XPATH, "//*[contains(@href,'/appointments')]")
    MNU_CALENDER = (By.XPATH, "//*[@id='toolbar']/div/div[1]/div/ul/li[1]/ul/li[2]/a")
    TXT_ADDNOTESt = (By.XPATH, '//*[@id="id_appt-notes"]')
    BTN_EVENT = (By.XPATH, '//*[@id="faddbtn"]')
    BTN_PRINT = (By.XPATH, "//i[@class='icon-print']")
    BTN_TODAY = (By.XPATH, '//*[@id="showtodaybtn"]')
    TXT_PATIENT_NAME = (By.ID, "id_appt-patient_autocomplete")
    TXT_PATIENT_ITEM = (By.XPATH, "/html/body/ul[4]/li")
    BTN_TIME = (By.XPATH, "//*[@class='controls']/following::input[@name='appt-scheduled_time_1']")
    BTN_DURATION = (
        By.XPATH,
        "//*[@class='controls']/following::input[@name='appt-scheduled_time_0']",
    )
    BTN_SAVE = (By.XPATH, '//*[@id="id_appt_submit_row"]/button[3]')
    BTN_DELET = (By.LINK_TEXT, "Delete")
    BTN_CLOSE_ARROW = (By.XPATH, '//a[@class="ui-dialog-titlebar-close ui-corner-all"]')
    TXT_REASON_PATIENT = (By.XPATH, '//textarea[@id="id_appt-reason"]')
    CHK_BREAK = (By.XPATH, '//*[@id="id_appt-appt_is_break"]')
    CHK_WALKIN = (By.XPATH, '//*[@id="id_appt-walk_in"]')
    CHK_TRANSITIONOFCARE = (By.XPATH, '//*[@id="id_appt-transition_of_care"]')
    CHK_REFRELL = (By.XPATH, '//*[@id="id_appt-referral_appointment"]')
    CHK_VIEWACTIVEREMIDER = (By.XPATH, '//*[@id="id_reminderCheckBox"]')
    CHK_REMIDERPROFILE = (By.XPATH, '//*[@id="id_reminderProfilesSelect"]')
    DDL_CHOSEREMIDER = (By.XPATH, '//*[@id="id_reminderProfilesSelect"]')
    CHK_NEWPATIENT = (By.XPATH, '//*[@id="id_appt-is_new_patient"]')
    TXT_FIRSTNAME = (By.XPATH, '//*[@id="id-patient_create_first_name"]')
    TXT_LASTNAME = (By.XPATH, '//*[@id="id-patient_create_last_name"]')
    BTN_ADD = (By.XPATH, '//*[@id="id_appt-new_patient_form_cell"]/button')
    DDL_REMINDERPROFILE = (By.XPATH, '//*[@id="id_reminderProfilesSelect"]')
    BTN_ADDNEWREMINDER = (By.XPATH, '//*[@id="id_add_simple_reminder"]')
    BTN_EDI = (By.XPATH, '//*[@id="id_customize_simple_reminder_profile"]/i')
    TXT_ADDTEXT = (By.XPATH, '//*[@id="id_reminder_custom_text_4"]')
    CHK_ARRANGEFOLLOWUP = (By.XPATH, '//*[@id="id_follow_up_appt_checkbox"]')
    CHK_FOLLOWUPDATE = (By.XPATH, '//*[@id="id_appt-follow_up_appointment_date"]')
    BTN_NXT = (
        By.XPATH,
        "//div[@class='ui-datepicker-title']/following::span[contains(text(),'Next')]",
    )
    TXT_REASON = (By.XPATH, '//*[@id="id_appt-follow_up_appointment_reason"]')
    BTN_SELECTMONTH = (By.XPATH, '//*[@id="showmonthbtn"]')
    BTN_SEELECTDATE = (By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/table/tbody/tr[3]/td[1]')
    BTN_CLANDERMONTH = (By.XPATH, '//*[@id="showmonthbtn"]')
    BTN_DATE = (By.XPATH, '//*[@id="bbit_cal_event_119718222"]/div[3]')
    BTN_ALERT = (By.XPATH, '//*[@id="fancyConfirm_ok"]')
    TXT_ADD_NOTES = (By.XPATH, '//*[@id="id_appt-notes"]')
    CHK_RECURRING_APP = (By.XPATH, '//input[@id="id_appt-recurring_appointment"]')
    BTN_SELECTALL = (By.XPATH, '//*[@id="id_row_appt-weekly"]/div/span/span[1]')
    BTN_NEVER_END = (By.XPATH, '//*[@id="id_appt-infinite_series"]')
    BTN_NEXT = (By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/div/a/span')
    BTN_LAST_APP = (By.XPATH, '//input[@name="appt-recur_end_date"]')
    BTN_LAST_APP_DATE = (By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/table/tbody/tr[3]/td[4]')
    BTN_DONE = (By.XPATH, '//button[contains(text(),"Done")]')
    CHK_MONDAY = (By.ID, "id_appt-weekly_on_monday")
    CHK_TUESDAY = (By.ID, "id_appt-weekly_on_thursday")
    BTN_EDIT_REMINDER = (By.XPATH, '//div[@id="id_rem_row_1"]//a[1]')
    TXT_CUSTOM_MSG = (By.XPATH, '//textarea[@id="id_reminder_custom_text_1"] ')
    DDL_SMSTEXT = (By.XPATH, '//*[@id="id_reminder_type_1"]')
    DDL_WEEKS = (By.XPATH, '//*[@id="id_reminder_unit_type_1"]')
    DDL_AFTER = (By.XPATH, '//*[@id="id_reminder_unit_before_or_after_1"]')
    BTN_PREVIEW = (By.XPATH, '//div[@id="id_rem_row_1"]//a[2]')
    BTN_CLOSE = (By.XPATH, '//*[@id="id_preview_reminder"]/div[3]/button')
    BTN_DELET_REMINDER = (By.XPATH, '//div[@id="id_rem_row_8"]//a[@id="id_remove_simple_reminder"]')
    DDL_EXAM = (By.XPATH, "//select[@name='appt-examination_room']")
    DDL_PROFILE = (By.XPATH, "//select[@id='id_appt-appointment_profile']")
    DDL_STATUS = (By.XPATH, '//*[@id="id_appt-appointment_status"]')


class CalnderLocators(object):
    """
    This class used to Schedule  appointment by  Event -locators
    """

    BTN_MONTH = (By.XPATH, '//*[@id="showmonthbtn"]/span')
    BTN_DAILY = (By.XPATH, "//button[@id='showdaybtn']")
    BTN_WEEKLY = (By.XPATH, "//span[@title='Week']")
    BTN_EXAM_ROOM = (By.XPATH, "//span[@title='Examroom']")
    BTN_DOCTOR = (By.XPATH, "//span[@title='Doctor']")
    BTN_SELECTMONTH = (By.XPATH, '//*[@id="id_inlineDatePicker"]/div/div/div/select[1]')
    BTN_EDIT = (By.XPATH, "//button[@title='Edit Patient']")
    TXT_FSTNAME = (By.CSS_SELECTOR, "#id_first_name")
    TXT_LSTNAME = (By.XPATH, '//*[@id="id_last_name"]')
    TXT_SUFFIX = (By.XPATH, "//input[@id='id_suffix']")
    TXT_LST_APP = (By.XPATH, '//*[@id="id_date_of_last_appointment"]')
    TXT_REMINDER = (By.XPATH, '//*[@id="id_language"]')
    BTN_SAVE_CLOSE = (By.XPATH, '//input[@value="Save & Close"]')
    BTN_DATE_ICON = (By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']")
    DDL_DATE = (By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/table/tbody/tr[3]/td[4]')
    BTN_TIME = (By.XPATH, "//span[@title='Decrement']")
    BTN_COLOR = (By.XPATH, '//*[@id="id_appt-custom_color"]')
    TXT_COLOR = (By.XPATH, "//div[@class='well scheduling_well']//tr[2]//td[4]")
    BTN_PRE_MONTH = (
        By.XPATH,
        "//span[@class='ui-icon ui-icon-circle-triangle-w'][contains(text(),'Prev')]",
    )
    BTN_NEXT_MONTH = (By.XPATH, "//span[contains(text(),'Next')]")
    BTN_PAST_DAY = (By.XPATH, "//div[@id='id_calendar_wrapper']//tr[3]//td[5]")
    DDL_YEAR = (By.XPATH, "//*[@id='id_inlineDatePicker']/div/div/div/select[2]")
    BTN_DAY = (By.XPATH, "//table[1]/tbody[1]/tr[3]/td[4]/a[1]")
    DDL_SELECT_OFF = (By.XPATH, "//select[@id='id_office']")
    TXT_STARTDATE = (By.XPATH, "//*[@name = 'start_date']")
    TXT_ENDDATE = (By.XPATH, "//input[@id='id_end_date']")
    BTN_DONE = (By.XPATH, "//button[contains(text(),'Done')]")
    BTN_DOCTORS_ALL = (By.XPATH, "//span[@class='select-all-doctors btn']")
    BTN_UPDATE = (By.XPATH, "//input[@value='Update Filters']")
    BTN_PRINT = (By.XPATH, "//input[@value='Print']")
    CHK_CELLPHONE = (By.XPATH, "//input[@id='id_print_cell']")
    CHK_EXAM_1 = (By.XPATH, "//input[@id='id_exam_room_1']")
    CHK_EXAM_2 = (By.XPATH, "//input[@id='id_exam_room_2']")
    DDL_FONT_SIZE = (By.XPATH, "//select[@id='id-fontsize']")
    BTN_ADD_PATIENT = (By.XPATH, '//*[@id="id_add_patient"]/i')
    BTN_ADD_OFFICE = (By.XPATH, '//*[@id="id_add_office"]/i')
    TXT_OFFICE = (By.XPATH, '//*[@id="id_name"]')
