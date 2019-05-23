from selenium.webdriver.common.by import By


class MainPageLocators(object):
    VALUATION_WINDOW = (By.XPATH, '//div[@class="NPS"]')
    VALUATION_CLOSE = (By.XPATH, '//div[@class="NPS__close"]')
    VALUATION_TITLE = (By.XPATH, '//div[@class="NPS__message"]')
    VALUATION_NOT_LIKE = (By.XPATH, '//div[@class="NPS__not-like-title"]')
    VALUATION_LIKE = (By.XPATH, '//div[@class="NPS__like-title"]')
    VALUATION = lambda val: f'//div[@class="NPS__button n{val}"]'

    COMMENT_TEXT = (By.XPATH, '//div[@class="NPS__feedback-title"]')
    COMMENT_TEXTAREA = (By.ID, 'feedbackTextarea')
    SEND_BUTTON = (By.XPATH, '//button[@class="NPS__feedback-send"]')
