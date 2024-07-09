import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage


class TestAddTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("url")
        time.sleep(20)
        cls.home_page = HomePage(cls.driver)
        cls.config = ConfigProvider()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_click_add_task_button(self):
        self.home_page.click_add_task_button()

        self.assertTrue(self.home_page.is_task_box_present())


if __name__ == '__main__':
    unittest.main()
