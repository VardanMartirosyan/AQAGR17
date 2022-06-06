import time
from Pages import SearchResultPage
from Pages import GoogleMainPage
from Pages import ImagesPage
from TestCases import BaseTest


class GoogleTest(BaseTest):
    def setUp(self):
        self.mainPage = GoogleMainPage.MainPage(self.driver)
        self.searchResultPage = SearchResultPage.SearchResultPageClass(self.driver)
        self.imagesPage = ImagesPage.ImagesPageClass(self.driver)
        self.driver.get(self.variables.mainURL)

    def test_mygoogletest(self):
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
