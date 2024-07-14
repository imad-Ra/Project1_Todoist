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


class TestRemoveTask(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json('../config.json')
        self.driver = self.browser.get_driver(self.config["Url"])
        time.sleep(10)
        login = LoginPage(self.driver)
        login.login_flow(self.config["Email"], self.config["Password"])

        self.home_page = HomePage(self.driver)
        self.home_page.click_add_task_button()

        add_task_page = TestAddRemoveTask(self.driver)
        add_task_page.click_add_task_button()

        text_to_insert = self.config["Title1_Test"]
        add_task_page.fill_task_name(text_to_insert)
        add_task_page.click_add_task_button()





    def tearDown(self):
        self.add_task_page = TestAddRemoveTask(self.driver)
        self.driver.quit()


    def test_remove_task_name(self):
        deleted_task_title = TestAddRemoveTask(self.driver)
        deleted_task_title.delete_task()

        #Assert
        self.assertTrue(deleted_task_title.verify_delete_task())


