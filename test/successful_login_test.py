import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
import time
from logic.login_page import LoginPage



class TestLogin(unittest.TestCase):

    #loading data from json file using config_provider
    config = ConfigProvider.load_config_json('../config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["Url"])
        time.sleep(5)



    def TearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        # Arrange
        # time.sleep(10)
        # email_login = LoginPage(self.driver)
        # email_login.fill_email(self.config["Email"])
        # self.driver.implicitly_wait(5)
        # password_login = LoginPage(self.driver)
        # # Act
        # password_login.fill_password(self.config["Password"])
        # self.driver.implicitly_wait(5)
        # login_button = LoginPage(self.driver)
        # login_button.click_sign_in_button()
        # time.sleep(10)
        # self.assertEqual(self.driver.current_url, self.config["home page"])

        # # Assert
        login = LoginPage(self.driver)
        login.login_flow(self.config["Email"], self.config["Password"])
        self.assertEqual(self.driver.current_url, self.config["home page"])





if __name__ == '__main__':
    unittest.main()
