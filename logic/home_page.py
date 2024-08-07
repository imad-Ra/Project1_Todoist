import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    HOME_ADD_TASK_BUTTON = '//button[@class="plus_add_button" and contains(text(), "Add task")]'
    TASK_BOX = '//li[@class="manager indent_1"]'
    TODAY_TEXT = '//h1[text()="Today"]'
    INBOX_SIDE_BAR_BUTTON = '//div[@role="navigation"]//li[@id="filter_inbox"]'
    INBOX_SECTION_BUTTON = '//li[@id="filter_inbox"]'

    MY_PROJECT_MENU_BUTTON = '//button[@aria-label="My projects menu"]'
    ADD_PROJECT_BUTTON = '//div[@role="menuitem" and @aria-label="Add project"]'
    ADD_PROJECT_NAME_INPUT = '//input[@id="edit_project_modal_field_name"]'
    ADD_PROJECT_NAME_SUBMIT_BUTTON = '//button[@type="submit"]'

    ACCOUNT_SETTINGS_BAR_BUTTON = '//button[@aria-label="Settings"]'

    # Account settings option in the settings bar
    ACCOUNT_SETTINGS_OPTIONS_BUTTON = "//div[@aria-label='Settings menu']//a[contains(@href,'/app/settings/account')]"

    GENERAL_BUTTON = "//a[@href='/app/settings/general']"
    LANGUAGE_SELECTOR = "//div[@data-testid='select-wrapper']//select[@name='language']"
    LANGUAGE_POP_UP_LIST = "//div[@data-testid='select-wrapper']//select[@name='language']/option"
    SELECT_DEUTSCH = "//select[@name='language']/option[text()='Deutsch']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_task_button(self):
        """
    this function click the task button in the home page.
        """
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.HOME_ADD_TASK_BUTTON))).click()

    def is_task_box_present(self):
        try:
            self._driver.find_element(By.XPATH, self.TASK_BOX)
            return True
        except NoSuchElementException:
            return False

    def click_my_projects_menu_button(self):
        self._my_project_menu_element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.MY_PROJECT_MENU_BUTTON))).click()
        time.sleep(5)

    def click_add_project_button(self):
        self._add_project_button = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ADD_PROJECT_BUTTON))).click()
        time.sleep(5)

    def click_add_project_name(self):
        self._add_project_name = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_PROJECT_NAME_INPUT))).click()

    def fill_add_project_name(self):
        self._add_project_name = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ADD_PROJECT_NAME_INPUT))).send_keys("Test1")

    def click_submit_add_project_button(self):
        self._submit_add_project_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_PROJECT_NAME_SUBMIT_BUTTON))).click()
        time.sleep(5)

    def add_project_flow(self):
        self.click_my_projects_menu_button()
        self.click_add_project_button()
        self.click_add_project_name()
        self.fill_add_project_name()
        self.click_submit_add_project_button()

    def click_inbox_section_button(self):
        self._inbox_section_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.INBOX_SECTION_BUTTON))).click()
        time.sleep(10)

    # Account settings bar
    def click_account_setting_bar_button(self):
        self._account_settings_bar_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.ACCOUNT_SETTINGS_BAR_BUTTON))).click()
        time.sleep(7)

    def click_account_setting_options_button(self):
        self._account_settings_options_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.ACCOUNT_SETTINGS_OPTIONS_BUTTON))).click()
        time.sleep(7)

    # For 10 test
    def click_inbox_side_bar_button(self):
        self._inbox_side_bar_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.INBOX_SIDE_BAR_BUTTON))).click()
        time.sleep(5)
