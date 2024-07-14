import unittest
import time
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.inbox_page import InboxSection
from logic.login_page import LoginPage


class TestAddSectionTitle(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json('../config.json')
        self.driver = self.browser.get_driver(self.config["Url"])
        time.sleep(10)
        login = LoginPage(self.driver)
        login.login_flow(self.config["Email"], self.config["Password"])
        self.home_page = HomePage(self.driver)
        self.inbox_page = InboxSection(self.driver)
        self.home_page.click_inbox_section_button()

    def tearDown(self):
        self.inbox_page.added_section_deletion_flow()
        self.driver.quit()

    def test_add_section_title(self):
        self.inbox_page.hover_over_section_line()
        self.inbox_page.click_on_add_section_line()

        # Use the section name from the config
        section_name = self.config["Section_name"]
        self.inbox_page.fill_name_this_section_input(section_name)

        self.inbox_page.click_add_section_button()

        verification_result = self.inbox_page.verify_section_name()
        self.assertEqual(verification_result, "task title matching")

