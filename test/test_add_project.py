
import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.project_page import ProjectPage
from infra.logging_basicConfig import LoggingSetup

class AddProject(unittest.TestCase):


    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json(r'C:\Users\nraba\PycharmProjects\Project1_Todoist\config.json')
        self.driver = self.browser.get_driver(self.config["Url"])
        login = LoginPage(self.driver)
        login.login_flow(self.config["Email"], self.config["Password"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()



    def test_add_project(self):
        self.home_page.add_project_flow()

        verify_added_project = ProjectPage(self.driver)
        self.assertTrue(verify_added_project.visible_project_header())



if __name__ == '__main__':
    unittest.main()