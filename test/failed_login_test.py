import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logging_basicConfig import LoggingSetup

import time
from logic.login_page import LoginPage


class TestLogin(unittest.TestCase):
    #loading data from json file using config_provider
    config = ConfigProvider.load_config_json(r'C:\Users\nraba\PycharmProjects\Project1_Todoist\config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["Url"])

    def TearDown(self):
        self.driver.quit()

    #Failed login testing . (Valid email , Unvalid password)
    def test_failed_login(self):
        login = LoginPage(self.driver)
        login.login_flow(self.config["Email"], self.config["WrongPass"])
        self.assertTrue(login.wrong_sign_in_message_is_displayed())


if __name__ == '__main__':
    unittest.main()
