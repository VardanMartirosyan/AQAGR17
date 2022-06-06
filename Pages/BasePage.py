import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators
from selenium.webdriver.common.keys import Keys
from Common.CustomFind import Find
from Common.Logger.LoggerFile import LoggerClass

class BasePageClass():
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators.LocatorsClass()
        self.find = Find.FindElementClass(self.driver)
        self.logger = LoggerClass()

    def find_element(self, *locator):
        return self.find.custom_find(*locator)

    def find_elements(self, *locator):
        self.wait_elements(locator)
        return self.driver.find_elements(*locator)

    def hover(self, locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_elements(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(locator))
        except:
            self.logger.add_log("ERROR", "Element {} not found".format(locator))
            print("ERROR: Element Not Found!!!")
            exit(2)
            self.driver.quit()


    def wait_element(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except:
            print("ERROR: Element Not Found!!!")
            self.driver.quit()
            exit(2)

    def get_title(self):
        return self.driver.title



