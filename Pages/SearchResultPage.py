from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.BasePage import BasePageClass


class SearchResultPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)

    def click_into_images_section(self):
        imagesSection = self.find_element(self.locators.imagesSectionLocator)
        imagesSection.click()

    def click_into_news_section(self):
        newsSection = self.driver.find_element(self.locators.newsSectionLocator)
        newsSection.click()

    def click_into_videos_section(self):
        videosSection = self.driver.find_element(self.locators.videosSectionLocator)
        videosSection.click()
