import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.login_page import LoginPage


class TestAddTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("url")
        time.sleep(20)
        cls.login_page = LoginPage(cls.driver)
        cls.config = ConfigProvider()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_login_successfully(self):
        email = self.config.get_value(self,"username")
        password = self.config.get_value(self,"password")
        self.login_page.login(email, password)

        self.assertTrue(self.login_page.is_sign_in_successful())

if __name__ == '__main__':
    unittest.main()
