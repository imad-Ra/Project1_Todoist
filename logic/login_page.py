from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from infra.base_page import BasePage


class LoginPage(BasePage):
    SIGN_IN_FIELDS = '//input'
    SIGN_IN_BUTTON = '//button[@type="submit"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._sign_in_fields = self._driver.find_elements(By.XPATH, self.SIGN_IN_FIELDS)
        self._email_field = self._sign_in_fields[0]
        self._password_field = self._sign_in_fields[1]
        self._sign_in_button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)

    def login(self, email, password):
        time.sleep(20)
        self._email_field.send_keys(email)
        self._password_field.send_keys(password)

    def click_sign_in_button(self):
        self._sign_in_button.click()

    def is_sign_in_successful(self):
        try:
            self._driver.find_element(By.XPATH, '')
            return True
        except NoSuchElementException:
            return False