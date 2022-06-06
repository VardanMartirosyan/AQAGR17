import time
from Pages import SearchResultPage
from Pages import GoogleMainPage
from Pages import ImagesPage
from TestCases.BaseTest import BaseTestClass


class GoogleTest(BaseTestClass):
    def setUp(self):
        self.logger.add_log("INFO", "_________________________________________________")
        self.logger.add_log("INFO", "Starting Test Case {}".format(type(self).__name__))
        self.logger.add_log("INFO", "_________________________________________________")
        self.mainPage = GoogleMainPage.MainPage(self.driver)
        self.searchResultPage = SearchResultPage.SearchResultPageClass(self.driver)
        self.imagesPage = ImagesPage.ImagesPageClass(self.driver)
        self.driver.get(self.variables.mainURL)

    def test_mygoogletest(self):
        self.assertEqual("Google", self.mainPage.get_title(), "ERROR: Match Error")
        self.mainPage.fill_search_field(self.variables.productName)
        time.sleep(2)
        self.mainPage.press_to_search_button()
        time.sleep(2)
        # self.searchResultPage.click_into_news_section()
        # time.sleep(2)
        # self.searchResultPage.click_into_videos_section()
        # time.sleep(2)
        self.searchResultPage.click_into_images_section()
        time.sleep(2)
        self.imagesPage.click_into_random_picture()
        time.sleep(3)
        self.logger.add_log("INFO", "Test Case '{}' Finished".format(type(self).__name__))


