import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage
from logic.home_page import HomePage
from logic.task_page import TestAddRemoveTask


class AccountSettings(BasePage):
    """
    A class representing the Account Settings page in the application.

    This class provides methods to interact with various settings on the Account Settings page,
    including language settings and quick add customization.
    """

    # XPATH constants for various elements on the page
    GENERAL_BUTTON = "//a[@href='/app/settings/general']"
    LANGUAGE_SELECTOR = "//div[@data-testid='select-wrapper']//select[@name='language']"
    LANGUAGE_POP_UP_LIST = "//div[@data-testid='select-wrapper']//select[@name='language']/option"
    SELECT_DEUTSCH_BUTTON = "//select[@name='language']/option[text()='Deutsch']"
    SELECT_ENGLISH_BUTTON = "//select[@name='language']/option[text()='English']"
    UPDATE_SETTINGS_BUTTON = '//button[@type="submit"]'
    DEUTSCH_POP_UP_LIST_SELECTED = "//select[@name='language']"
    LANGUAGE_IN_DEUTSCH_LANGUAGE = "//span[text()='Sprache']"

    QUICK_ADD_BUTTON = "//a[@href='/app/settings/quick-customization']"
    ADD_LOCATION_TO_QUICK_ADD_BUTTON = '//button[@aria-label="Add location to Quick Add"]'
    REMOVE_LOCATION_FROM_QUICK_ADD_BUTTON = '//button[@aria-label="Remove location from Quick Add"]'
    UPDATE_BUTTON = '//button[@type="submit"]'
    CLOSE_SETTINGS_BUTTON = '//button[@aria-label="Close settings"]'

    def __init__(self, driver):
        """
        Initialize the AccountSettings page object.

        Args:
            driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)
        self._TestAddRemoveTask = TestAddRemoveTask(driver)
        self.driver = driver
        self._HomePage = HomePage(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def click_general_button(self):
        """Click the general settings button."""
        self._general_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.GENERAL_BUTTON))).click()
        time.sleep(5)

    def click_language_selector(self):
        """Click the language selector dropdown."""
        self._language_selector = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.LANGUAGE_SELECTOR))).click()
        time.sleep(5)

    def select_deutsch_button(self):
        """Select the German language option."""
        self._deutsch_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.SELECT_DEUTSCH_BUTTON))).click()
        time.sleep(5)

    def click_update_settings_button(self):
        """Click the update settings button."""
        self._update_settings_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.UPDATE_SETTINGS_BUTTON))).click()
        time.sleep(5)

    def change_language_to_deutsch_flow(self):
        """Execute the flow to change the language to German."""
        self._HomePage.click_account_setting_bar_button()
        self._HomePage.click_account_setting_options_button()
        self.click_general_button()
        self.click_language_selector()
        self.select_deutsch_button()
        self.click_update_settings_button()

    def verify_deutsch_selected_language(self):
        """
        Verify if the German language is selected.

        Returns:
            bool: True if German is selected, False otherwise.
        """
        try:
            language = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.LANGUAGE_IN_DEUTSCH_LANGUAGE)))
            return language.is_displayed()
        except NoSuchElementException:
            return False

    def select_english_button(self):
        """Select the English language option."""
        self._english_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.SELECT_ENGLISH_BUTTON))).click()
        time.sleep(5)

    def change_language_to_english_flow(self):
        """Execute the flow to change the language back to English."""
        self.click_general_button()
        self.click_language_selector()
        self.select_english_button()
        self.click_update_settings_button()

    def click_quick_add_button(self):
        """Click the quick add customization button."""
        self._quick_add_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.QUICK_ADD_BUTTON))).click()
        time.sleep(5)

    def click_add_location_to_quick_add_button(self):
        """Click the button to add location to quick add."""
        self._add_location_to_quick_add_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_LOCATION_TO_QUICK_ADD_BUTTON))).click()
        time.sleep(5)

    def click_update_button(self):
        """Click the update button."""
        self._click_update_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.UPDATE_BUTTON))).click()
        time.sleep(5)

    def click_close_settings_button(self):
        """Click the close settings button."""
        self._close_settings_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.CLOSE_SETTINGS_BUTTON))).click()
        time.sleep(5)

    def add_location_to_quick_add_flow(self):
        """Execute the flow to add location to quick add."""
        self._HomePage.click_account_setting_bar_button()
        self._HomePage.click_account_setting_options_button()
        self.click_quick_add_button()
        self.click_add_location_to_quick_add_button()
        self.click_update_button()
        self.click_close_settings_button()
        self._HomePage.click_add_task_button()
        self._HomePage.click_inbox_side_bar_button()
        self._HomePage.click_add_task_button()

    def verify_location_added_to_quick_add_flow(self):
        """
        Verify if the location was successfully added to quick add.

        Returns:
            bool: True if location is added, False otherwise.
        """
        return self._TestAddRemoveTask.verify_location_button()



    def click_remove_location_from_quick_add_button(self):
        """Click the button to remove location from quick add."""
        self._remove_location_from_quick_add_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.REMOVE_LOCATION_FROM_QUICK_ADD_BUTTON))).click()
        time.sleep(5)

    def remove_location_from_quick_add_flow(self):
        """Execute the flow to remove location from quick add."""
        self._HomePage.click_account_setting_bar_button()
        self._HomePage.click_account_setting_options_button()
        self.click_quick_add_button()
        self.click_remove_location_from_quick_add_button()
        self.click_update_button()