import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.task_page import TestAddRemoveTask
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.account_settings import AccountSettings



class TestChangeLanguage(unittest.TestCase):
    # config = ConfigProvider.load_config_json('../config.json')

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.account_settings = None

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json('../config.json')
        self.driver = self.browser.get_driver(self.config["Url"])
        time.sleep(10)
        login = LoginPage(self.driver)
        login.login_flow(self.config["Email"], self.config["Password"])
        self.home_page = HomePage(self.driver)
        self.AccountSettings = AccountSettings(self.driver)
        self.account_settings = AccountSettings(self.driver)  # Assuming AccountSettings is your page object




    def tearDown(self):
        self.AccountSettings.change_language_to_english_flow()
        self.driver.quit()

    def test_add_section_title(self):
        self.AccountSettings.change_language_to_deutsch_flow()

        verification_result = self.account_settings.verify_deutsch_selected_language()
        self.assertTrue(verification_result)
