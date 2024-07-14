import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.account_settings import AccountSettings
from logic.home_page import HomePage
from logic.login_page import LoginPage


class QuickAddButton(unittest.TestCase):
    """
    Test class for the QuickAddButton.
    The test is for adding a location to the quick add flow.
    """
    def setUp(self):
        """
        Set up the test by initializing the browser, loading configuration,
        logging in, and navigating to the home page.
        """
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json('../config.json')
        self.driver = self.browser.get_driver(self.config["Url"])
        time.sleep(10)
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

    def test_add_section_title(self):
        """
        Test the add_section_title method.
        """
        # Arrange
        self.AccountSettings.add_location_to_quick_add_flow()

        # Act
        # (The act is implicitly part of the add_location_to_quick_add_flow method)

        # Assert
        self.assertTrue(self.AccountSettings.verify_location_added_to_quick_add_flow(),
                        "Location was not successfully added to quick add flow")
