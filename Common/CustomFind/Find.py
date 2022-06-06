from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.Logger.LoggerFile import LoggerClass


class FindElementClass():
    def __init__(self, driver):
        self.driver = driver
        self.logger = LoggerClass()


    def custom_find(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except:
            self.logger.add_log("ERROR", "Element {} not found".format(locator))
            exit(2)
