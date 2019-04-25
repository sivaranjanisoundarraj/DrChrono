import unittest
from selenium import webdriver
import HtmlTestRunner
import os
from src.main.pages import *


class TestBase(unittest.TestCase):
    'Initilization and closure  of driver for each class - Globally'
    @classmethod
    def setUpClass(cls):
        super(TestBase, cls).setUpClass()
        try:
            project_root = os.path.dirname(os.path.dirname(__file__))
            output_path = os.path.join(project_root, 'driver')
            chrome_path = os.path.join(output_path, 'chromedriver.exe').replace('\\', '/')
            print(chrome_path)
            cls.driver = webdriver.Chrome(chrome_path)
            cls.driver.implicitly_wait(20)
            cls.driver.maximize_window()
        except BaseException:
            cls.fail("Could not setup Class")

    @classmethod
    def tearDownClass(cls):
        super(TestBase, cls).tearDownClass()
        cls.driver.save_screenshot("failure.png")
        cls.driver.quit()