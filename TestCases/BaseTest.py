import unittest
from selenium import webdriver
from Common.Variables import Variables
from Common.Logger.LoggerFile import LoggerClass


class BaseTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Safari()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.delete_all_cookies()
        cls.variables = Variables.ProjectVariables()
        cls.logger = LoggerClass()


    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()
        cls.driver.quit()

