from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from infra.base_page import BasePage
import time


class InboxSection(BasePage):
    ADD_SECTION_LINE = '//button[@type="button" and @class="hover_action_button"]'
    NAME_THIS_SECTION_INPUT = '//input[@placeholder="Name this section"]'
    ADD_SECTION_BUTTON = '//button[@type="submit"]'
    ADDED_SECTION_NAME = '//button/span[@class="simple_content"]'
    # 3 dots near the section name
    EDIT_SECTION_MENU_BUTTON = '//button[@aria-label="section menu"]'
    DELETE_SECTION_MENU_BUTTON = '//div[@role="menuitem"][contains(., "Delete")]'
    CONFIRM_SECTION_MENU_DELETION_BUTTON = '//button[.//span[text()="Delete"]]'
    EMPTY_INBOX_PAGE_IMAGE = '//img[@src="https://todoist.b-cdn.net/assets/images/f6fa2d79a28b6cf1c08d55511fee0c5b.png"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def hover_over_section_line(self):
        ActionChains(self._driver).move_to_element(self._driver.find_element(By.XPATH, self.ADD_SECTION_LINE)).perform()

    def click_on_add_section_line(self):
        self._section_line = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_SECTION_LINE))).click()
        time.sleep(5)

    def fill_name_this_section_input(self, section_name):
        self._name_this_section_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.NAME_THIS_SECTION_INPUT))).send_keys(section_name)
        time.sleep(5)

    def click_add_section_button(self):
        self._add_section_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_SECTION_BUTTON))).click()
        time.sleep(5)

    def verify_section_name(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.ADDED_SECTION_NAME)))
            return "task title matching"
        except NoSuchElementException:
            return False

    def click_edit_section_button(self):
        self._more_actions_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.EDIT_SECTION_MENU_BUTTON))).click()
        time.sleep(15)

    def click_section_delete_button(self):
        self._section_delete_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.DELETE_SECTION_MENU_BUTTON))).click()
        time.sleep(15)

    def click_section_confirm_delete_button(self):
        self._project_confirm_delete_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.CONFIRM_SECTION_MENU_DELETION_BUTTON))).click()
        time.sleep(15)

    def added_section_deletion_flow(self):
        self.click_edit_section_button()
        self.click_section_delete_button()
        self.click_section_confirm_delete_button()

    def visible_empty_inbox_page(self):
        try:
            self._empty_inbox_page = WebDriverWait(self._driver , 10).until(EC.presence_of_element_located((By.XPATH, self.EMPTY_INBOX_PAGE_IMAGE )))
            return True
        except NoSuchElementException:
            return False





