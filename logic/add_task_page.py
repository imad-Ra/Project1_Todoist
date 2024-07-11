from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from infra.base_page import BasePage
from logic.home_page import HomePage


class AddTask(BasePage):
    TASK_NAME_INPUT = '//p[@data-placeholder="Task name"]'

    def __init__(self, driver):
        super().__init__(driver)

    def fill_task_name(self):
        element = WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.XPATH, self.TASK_NAME_INPUT)))
        element.send_keys("Test Try Task1")

    def add_task_flow(self):
        self.fill_task_name()
