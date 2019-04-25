from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import os
import time


class BaseBage(object):
    """
    This is base web action class
    """

    def __init__(self, driver):
        """
        constructor of class
        @param self : this is refer to instance of object
        """
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        """
        This method used to find element
        @param locator : get locator from locators module
        """
        return self.driver.find_element(*locator)

    def click(self, *locator):
        """
        This method is used to click the element
        :@param driver :get locator from locators module
        """
        try:
            element = self.find_element(*locator)
            time.sleep(2)
            element.click()
        except WebDriverException:
            self.fail("Could not click the element")

    def type(self, value, *locator):
        """
        This method is used to enter the value
        :@param driver :get locator from locators module
        """
        try:
            element = self.driver.find_element(*locator)
            element.clear()
            element.send_keys(value)
        except WebDriverException:
            self.fail("Could not enter value to text box" )

    def clear(self, *locator):
        """
        This method is used to enter the value
        :@param driver :get locator from locators module
        """
        try:
            element = self.find_element(*locator)
            element.clear()
        except WebDriverException:
            self.fail("Could not clear the text box value")

    def selectByVisibleText(self, texttoselect, *locator):
        """
        This method is used to Select the VisibleText
        :@param driver :get locator from locators module
        """
        try:
            select_element = Select(self.driver.find_element((*locator)))
            select_element.select_by_visible_text(texttoselect)
        except WebDriverException:
            self.fail("Could not selectBy visible text")

    def hover(self, *locator):
        """
        This method is used to hover the element
        :@param driver :get locator from locators module
        """
        try:
            element = self.find_element(*locator)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
        except WebDriverException:
            self.fail("Could not hover the element")

    def getText(self, *locator):
        """
        This method is used the get text from text box
        :@param driver :get locator from locators module
        """
        try:
            element = self.find_element(*locator)
            value = element.text
            return value
        except WebDriverException:
            self.fail("Could not get the value from text box")

    def isSelected(self, *locators):
        """
        This method is used the isSelected
        :@param driver :get locator from locators module
        """
        try:
            element = self.find_element(*locators)
            element.is_selected
            self.find_element(*locators).click()
        except WebDriverException:
            self.fail("Could not check")

    def scroll(self, *locators):
        """
        This method is used the scroll the element
        :@param driver :get locator from locators module
        """
        try:
            element = self.driver.find_element(*locators)
            time.sleep(5)
            self.driver.execute_script("return arguments[0].scrollIntoView();", element)
            assert True
        except:
            assert False

    def handlealert(self):
        """
        This method is used the handle alert
        :@param driver :get locator from locators module
        """
        try:
            obj = self.driver.switch_to_alert()
            obj.accept()
            assert True
        except:
            assert False
 
    def getAttribute(self, *locators):
        """
        This method is used the get the attribute value
        :@param driver :get locator from locators module
        """
        try:
            element = self.driver.find_element(*locators).get_attribute("value")
            return element
        except:
            assert False
