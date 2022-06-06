from Locators import Locators
import random
from Pages.BasePage import BasePageClass

class ImagesPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators.LocatorsClass()


    def click_into_random_picture(self, number=random.randint(1,20)):
        # randomPictureElement = self.driver.find_element(*self.locators.randomPictureElementLocator)
        # randomPictureElement.click()
        picturesElementsFromGoogle = self.find_elements(*self.locators.googleImagesElementsLocator)
        picturesElementsFromGoogle[number].click()


