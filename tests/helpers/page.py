from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from .locators import *
from .elements import *


class FeedbackText(MainPageElement):
    locator = MainPageLocators.COMMENT_TEXTAREA

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    feedback = FeedbackText()

    def get_valuation_window(self):
        element = self.driver.find_element(*MainPageLocators.VALUATION_WINDOW)
        return element

    def exist_valuation_window(self):
        exist = False
        try:
            self.get_valuation_window()
            exist = True
        except:
            pass

        return exist

    def click_close(self):
        element = self.driver.find_element(*MainPageLocators.VALUATION_CLOSE)
        element.click()

    def click_valuation(self, valuation):
        element = self.driver.find_element_by_xpath(MainPageLocators.VALUATION(valuation))
        element.click()

    def click_send(self):
        element = self.driver.find_element(*MainPageLocators.SEND_BUTTON)
        element.click()
