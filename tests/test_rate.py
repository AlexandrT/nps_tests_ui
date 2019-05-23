import pytest
import logging
import time
from selenium.common.exceptions import NoSuchElementException

from helpers.utils import *
from helpers.page import *
from helpers.support.assertions import *


logger = logging.getLogger('ui_site')
PATH = ''

class TestRate:
    """Test rate"""

    def setup_class(cls):
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    @pytest.mark.skip
    def test_cookie(self, selenium, main_url):
        """window exists if NPS_sended = 1 and frequency of show window"""

        repeat = 100

        counter = 0
        for i in range(repeat):
            selenium.delete_all_cookies()
            selenium.get(f"{main_url}{PATH}")
            main_page = MainPage(selenium)
            if main_page.exist_valuation_window():
                assert selenium.get_cookie('NPS_sended') == None
                counter += 1
            else:
                assert selenium.get_cookie('NPS_sended')['value'] == '1'


        assert counter == repeat/10

    def test_close_window(self, selenium, main_url):
        """close window on first screen"""

        while True:
            selenium.delete_all_cookies()
            selenium.get(f"{main_url}{PATH}")
            main_page = MainPage(selenium)

            if main_page.exist_valuation_window():
                main_page.click_close()
                time.sleep(2)

                if selenium.get_cookie('NPS_sended'):
                    assert selenium.get_cookie('NPS_sended')['value'] == '1'
                else:
                    raise AssertionError('Cookie NPS_sended does not contained')

                assert main_page.get_valuation_window().is_displayed() == False
                break

    @pytest.mark.parametrize(
        "user_action",
        [
            ("7"),
            ("10")
        ]
    )
    def test_send_positive(self, selenium, main_url, connect_to_db, user_action):
        """send positive valuation"""

        while True:
            selenium.delete_all_cookies()
            selenium.get(f"{main_url}{PATH}")
            main_page = MainPage(selenium)

            if main_page.exist_valuation_window():
                main_page.click_valuation(user_action)
                time.sleep(2)

                if selenium.get_cookie('NPS_sended'):
                    assert selenium.get_cookie('NPS_sended')['value'] == '1'
                else:
                    raise AssertionError('Cookie NPS_sended does not contained')

                assert main_page.get_valuation_window().is_displayed() == False
                assert_from_db(connect_to_db, user_action, None)
                break

    @pytest.mark.parametrize(
        "user_action, feedback",
        [
            ("6", f"test{int(time.time())}"),
            ("5", f"test{int(time.time())}"),
            ("0", f"test{int(time.time())}"),
            ("4", f"test{int(time.time())}\n\ntest"),
            ("2", f"   test{int(time.time())}  ")
        ]
    )
    def test_send_negative(self, selenium, main_url, connect_to_db, user_action, feedback):
        """send negative valuation"""

        while True:
            selenium.delete_all_cookies()
            selenium.get(f"{main_url}{PATH}")
            main_page = MainPage(selenium)

            if main_page.exist_valuation_window():
                main_page.click_valuation(user_action)
                main_page.feedback = feedback
                main_page.click_send()
                time.sleep(2)

                if selenium.get_cookie('NPS_sended'):
                    assert selenium.get_cookie('NPS_sended')['value'] == '1'
                else:
                    raise AssertionError('Cookie NPS_sended does not contained')

                assert main_page.get_valuation_window().is_displayed() == False
                assert_from_db(connect_to_db, user_action, feedback.strip())
                break

    def test_negative_without_comment(self, selenium, main_url, connect_to_db):
        """send negative valuation without comment"""

        user_action = "3"
        while True:
            selenium.delete_all_cookies()
            selenium.get(f"{main_url}{PATH}")
            main_page = MainPage(selenium)

            if main_page.exist_valuation_window():
                main_page.click_valuation(user_action)
                main_page.click_send()
                time.sleep(2)

                if selenium.get_cookie('NPS_sended'):
                    assert selenium.get_cookie('NPS_sended')['value'] == '1'
                else:
                    raise AssertionError('Cookie NPS_sended does not contained')

                assert main_page.get_valuation_window().is_displayed() == False
                assert_from_db(connect_to_db, user_action, None)
                break

    def test_close_on_comment_page(self, selenium, main_url, connect_to_db):
        """close window on comment page"""

        user_action = "1"
        feedback = f"test{int(time.time())}"
        while True:
            selenium.delete_all_cookies()
            selenium.get(f"{main_url}{PATH}")
            main_page = MainPage(selenium)

            if main_page.exist_valuation_window():
                main_page.click_valuation(user_action)
                main_page.feedback = feedback
                main_page.click_close()
                time.sleep(2)

                if selenium.get_cookie('NPS_sended'):
                    assert selenium.get_cookie('NPS_sended')['value'] == '1'
                else:
                    raise AssertionError('Cookie NPS_sended does not contained')

                assert main_page.get_valuation_window().is_displayed() == False

                with pytest.raises(AssertionError):
                    assert_from_db(connect_to_db, user_action, feedback)

                break
