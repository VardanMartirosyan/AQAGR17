import time
from Locators import Locators
from selenium.webdriver.common.keys import Keys
from Common.CustomFind import Find
from Pages.BasePage import BasePageClass


class MainPage(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators.LocatorsClass()

    def fill_search_field(self, argument):
        self.logger.add_log("INFO", "Called fill search field method")
        searhField = self.find.custom_find(self.locators.searchFieldLocator)
        searhField.clear()
        searhField.send_keys(argument)
        time.sleep(2)
        searhField.send_keys(Keys.ESCAPE)

    def press_to_search_button(self):
        self.logger.add_log("INFO", "Called press to search button method")
        googleSearchButton = self.find.custom_find(self.locators.googleSearchButtonLocator)
        googleSearchButton.click()
