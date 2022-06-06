from Locators import Locators
from selenium.webdriver.common.keys import Keys

class VideosSectionClass():
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators.LocatorsClass()

