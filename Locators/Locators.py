import random
from selenium.webdriver.common.by import By

class LocatorsClass():
    #GoogleMainPage Locators
    searchFieldLocator = (By.NAME, "q")
    googleSearchButtonLocator = (By.XPATH, "(//input[@class='gNO89b'])[2]")

    #NavigationBarLocagtors
    imagesSectionLocator = (By.LINK_TEXT, "Images")
    newsSectionLocator = (By.LINK_TEXT, "News")
    videosSectionLocator = (By.LINK_TEXT, "Videos")
    #ImagesSection Locators
    randomPictureElementLocator = (By.XPATH, "(//*[@class='rg_i Q4LuWd'])[" + str(random.randint(1, 20)) + "]")
    googleImagesElementsLocator = (By.XPATH, "//img[@class='rg_i Q4LuWd']")
    # googleImagesElementsLocator = (By.CLASS_NAME, "rg_i Q4LuWd")

class NavigationBarLocatorsClass():
    #NavigationBarLocagtors
    imagesSectionLocator = (By.LINK_TEXT, "Images")
    newsSectionLocator = (By.LINK_TEXT, "News")
    videosSectionLocator = (By.LINK_TEXT, "Videos")

