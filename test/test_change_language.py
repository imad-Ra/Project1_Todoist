import unittest
import logging
from infra.logging_basicConfig import LoggingSetup

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.account_settings_page import AccountSettings


class TestChangeLanguage(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json(r'C:\Users\nraba\PycharmProjects\Project1_Todoist\config.json')
        self.driver = self.browser.get_driver(self.config["Url"])
        login = LoginPage(self.driver)
        login.login_flow(self.config["Email"], self.config["Password"])
        self.home_page = HomePage(self.driver)
        self.AccountSettings = AccountSettings(self.driver)
        self.account_settings = AccountSettings(self.driver)
        logging.info("Setup completed")

    def tearDown(self):
        self.AccountSettings.change_language_to_english_flow()
        self.driver.quit()
        logging.info("Teardown completed")
        logging.info("Finished test_add_section_title")

    def test_add_section_title(self):
        logging.info("Starting test_add_section_title")

        self.AccountSettings.change_language_to_deutsch_flow()
        verification_result = self.account_settings.verify_deutsch_selected_language()

        self.assertTrue(verification_result, "Deutsch was not successfully set as the selected language")

        if verification_result:
            logging.info("Test passed: Deutsch successfully set as the selected language")
        else:
            logging.error("Test failed: Deutsch was not successfully set as the selected language")

