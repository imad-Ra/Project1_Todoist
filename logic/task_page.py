import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from logic.home_page import HomePage


class TestAddRemoveTask(BasePage):
    TASK_NAME_INPUT = '//p[@data-placeholder="Task name"]'
    SUBMIT_ADD_TASK_BUTTON = '//button[@data-testid="task-editor-submit-button"]'
    TASK_TITLE = '//div[@class="task_content"]'[1]
    ADDED_TASK = '//ul["@class = items"]//div[@context="[object Object]"]'
    TASK_LOCATION_BUTTON = '//div[@aria-label="Add location reminders"]'
    DELETE_TASK_BUTTON = '//button[@data-action-hint="task-complete"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_task_name(self, task_text):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.TASK_NAME_INPUT)))
        element.send_keys(task_text)

    def click_add_task_button(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.SUBMIT_ADD_TASK_BUTTON))).click()
        time.sleep(3)

    def get_current_task_name(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.TASK_TITLE))).text

    def verify_added_task(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.ADDED_TASK)))
            return "task Added"
        except NoSuchElementException:
            return False

    def delete_task(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.DELETE_TASK_BUTTON))).click()
        time.sleep(5)

    def verify_delete_task(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.ADDED_TASK)))
            return True
        except NoSuchElementException:
            return False

    def verify_location_button(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.TASK_LOCATION_BUTTON)))
            return True
        except NoSuchElementException:
            return False
