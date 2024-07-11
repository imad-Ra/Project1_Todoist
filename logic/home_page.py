from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from infra.base_page import BasePage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class WebDriverPage:



class HomePage(BasePage):

    ADD_TASK_BUTTON = '//button[@class="plus_add_button"]'
    TASK_BOX = '//li[@class="manager indent_1"]'
    TODAY_TEXT = '//h1[text()="Today"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_task_button = self._driver.find_element(By.XPATH,self.ADD_TASK_BUTTON)

    def click_add_task_button(self):
        """
    this function click the task button in the home page.
        """
        self._add_task_button.click()

    # def click_task_name ??


    # def add_task_flow(self):
    #     self.click_add_task_button()
    #     self.fill_task_name()


    def is_task_box_present(self):
        try:
            self._driver.find_element(By.XPATH, self.TASK_BOX)
            return True
        except NoSuchElementException:
            return False