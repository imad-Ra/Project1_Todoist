import unittest


from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.task_page import TestAddRemoveTask
from logic.home_page import HomePage
from logic.login_page import LoginPage
from infra.logging_basicConfig import LoggingSetup


class TestAddTask(unittest.TestCase):
    # config = ConfigProvider.load_config_json('../config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json(r'C:\Users\nraba\PycharmProjects\Project1_Todoist\config.json')
        self.driver = self.browser.get_driver(self.config["Url"])
        login = LoginPage(self.driver)
        login.login_flow(self.config["Email"], self.config["Password"])

        self.home_page = HomePage(self.driver)
        self.home_page.click_add_task_button()

    def tearDown(self):
        self.add_task_page = TestAddRemoveTask(self.driver)
        deleted_task_title = TestAddRemoveTask(self.driver)
        deleted_task_title.delete_task()
        self.driver.quit()

    def test_add_task_name(self):
        add_task_page = TestAddRemoveTask(self.driver)
        add_task_page.click_add_task_button()

        #Act
        text_to_insert = self.config["Title1_Test"]
        add_task_page.fill_task_name(text_to_insert)
        add_task_page.click_add_task_button()
        added_task_title = TestAddRemoveTask(self.driver)

        #Assert
        self.assertEqual("task Added", added_task_title.verify_added_task())
