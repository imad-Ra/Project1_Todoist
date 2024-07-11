import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.add_task_page import AddTask
from logic.home_page import HomePage
from logic.login_page import LoginPage


class TestAddTask(unittest.TestCase):
    config = ConfigProvider.load_config_json('../config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["Url"])
        time.sleep(10)
        login = LoginPage(self.driver)
        login.login_flow(self.config["Email"], self.config["WrongPass"])

    def TearDown(self):
        self.driver.quit()

    def test_add_task_name(self):
        time.sleep(3)
        add_text = AddTask(self.driver)
        add_text.add_task_flow()
