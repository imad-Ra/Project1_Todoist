import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
import time
from logic.login_page import LoginPage
from infra.logging_basicConfig import LoggingSetup



class TestLogin(unittest.TestCase):

    #loading data from json file using config_provider
    config = ConfigProvider.load_config_json(r'C:\Users\nraba\PycharmProjects\Project1_Todoist\config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["Url"])



    def TearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        # Arrange

        # # Assert
        login = LoginPage(self.driver)
        login.login_flow(self.config["Email"], self.config["Password"])
        self.assertEqual(self.driver.current_url, self.config["home page"])





if __name__ == '__main__':
    unittest.main()
