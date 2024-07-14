import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from infra.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


class ProjectPage(BasePage):
    PROJECT_PAGE_HEADER = '//div[@data-testid="large-header"]'
    # three dots button
    MORE_PROJECT_ACTIONS_BUTTON = '//button[@aria-label="Project options menu"]'
    PROJECT_DELETE_BUTTON = '//div[@role="menuitem"][contains(., "Delete")]'
    PROJECT_CONFIRM_DELETE_BUTTON = '//button[.//span[text()="Delete"]]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._more_project_actions_button = self._driver.find_element(By.XPATH, self.MORE_PROJECT_ACTIONS_BUTTON)

    def visible_project_header(self):
        try:
            self._project_header = WebDriverWait(self._driver , 10).until(EC.presence_of_element_located((By.XPATH, self.PROJECT_PAGE_HEADER )))
            return True
        except NoSuchElementException:
            return False

    def click_more_actions_button(self):
        self._more_actions_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH , self.MORE_PROJECT_ACTIONS_BUTTON))).click()
        time.sleep(15)

    def click_project_delete_button(self):
        self._project_delete_button = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.PROJECT_DELETE_BUTTON))).click()
        time.sleep(15)
    def click_project_confirm_delete_button(self):
        self._project_confirm_delete_button = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.PROJECT_CONFIRM_DELETE_BUTTON))).click()
        time.sleep(15)

    def added_project_deletion_flow(self):
        self.click_more_actions_button()
        self.click_project_delete_button()
        self.click_project_confirm_delete_button()


