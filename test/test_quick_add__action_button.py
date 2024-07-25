import unittest
import logging
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.account_settings_page import AccountSettings
from logic.home_page import HomePage
from logic.login_page import LoginPage


class QuickAddButton(unittest.TestCase):
    """
    Test class for the QuickAddButton. - Quick Add location button
    The test is for adding a location to the quick add flow.
    """

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json(r'C:\Users\nraba\PycharmProjects\Project1_Todoist\config.json')
        self.driver = self.browser.get_driver(self.config["Url"])
        login = LoginPage(self.driver)
        login.login_flow(self.config["Email"], self.config["Password"])
        self.home_page = HomePage(self.driver)
        self.AccountSettings = AccountSettings(self.driver)
        self.account_settings = AccountSettings(self.driver)

    def tearDown(self):
        """
        Clean up after each test by removing a location from the quick add flow
        and quitting the WebDriver.
        """
        self.AccountSettings.remove_location_from_quick_add_flow()
        self.driver.quit()
        logging.info("adding a location to the quick add flow test test completed")
        logging.info("______________")

    def test_add_location_to_quick_add_actions(self):
        """
        Test adding a location to the quick add flow.
        """
        logging.info("______________")
        logging.info("Starting adding a location to the quick add flow test")

        self.AccountSettings.add_location_to_quick_add_flow()

        self.AccountSettings.check_if_location_added_to_quick_add_flow()
        assertion_result = self.AccountSettings.verify_location_added_to_quick_add_flow()
        self.assertTrue(assertion_result, "Location was not successfully added to quick add flow")

        # Logger info
        if not assertion_result:
            logging.error("adding a location to the quick add flow test test failed")
