import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from infra.config_provider import ConfigProvider


class LoginPage(BasePage):
    EMAIL_INPUT = '//input[@id="element-0"]'
    PASSWORD_INPUT = '//input[@id="element-3"]'
    SIGN_IN_BUTTON = '//button[@type="submit"]'
    WRONG_SIGN_IN_MESSAGE = '//div[text()="Wrong email or password."]'

    config = ConfigProvider.load_config_json('../config.json')
    """
    A page object representing the login page.
    
    """

    def __init__(self, driver):
        super().__init__(driver)
        self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._sign_in_button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)

    def fill_email(self, email):
        self._email_input.send_keys(email)

    def fill_password(self, password):
        self._password_input.send_keys(password)

    def click_sign_in_button(self):
        self._sign_in_button.click()

    def login_flow(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_sign_in_button()
        time.sleep(10)

    def wrong_sign_in_message_is_displayed(self):
        self._wrong_sign_in_message = WebDriverWait(self._driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, self.WRONG_SIGN_IN_MESSAGE)))
        if self._wrong_sign_in_message.is_displayed():
            print("Wrong email or password.")
            return True
        print("test failed , it should show - Wrong email or password.- .")
# ____________________________
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium.common import NoSuchElementException


# # def fill_email_input(self, email):
# #     """
#     Fill in the username input field with the provided username.
#
#     :param username: The username to enter into the email input field.
#     """
#     element = WebDriverWait(self._driver, 5).until(
#         EC.presence_of_element_located((By.XPATH, self.EMAIL_INPUT)))
#     element.send_keys(email)


