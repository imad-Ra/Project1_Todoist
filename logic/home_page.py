from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class HomePage(BasePage):

    ADD_TASK_BUTTON = '//button[@class="plus_add_button"]'
    TASK_BOX = '//li[@class="manager indent_1"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_task_button = self._driver.find_element(By.XPATH,self.ADD_TASK_BUTTON)

    def click_add_task_button(self):
        self._add_task_button.click()

    def is_task_box_present(self):
        try:
            self._driver.find_element(By.XPATH, self.TASK_BOX)
            return True
        except NoSuchElementException:
            return False