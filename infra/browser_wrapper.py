from pip._internal.resolution.resolvelib.factory import C
from selenium import webdriver
from infra.config_provider import ConfigProvider

class BrowserWrapper:
    """
    A wrapper class for managing WebDriver instances.
    This class handles the creation and configuration of WebDriver instances
    based on the settings specified in a configuration file.
    """

    def __init__(self):
        """
        Initialize the BrowserWrapper object.

        Loads the configuration from a JSON file.
        """
        self._driver = None
        self.config = ConfigProvider.load_config_json('../config.json')

    def get_driver(self, url):
        """
        Create and return a WebDriver instance for the specified browser type.

        Args:
            url (str): The URL to navigate to after creating the driver.

        Returns:
            WebDriver: The created WebDriver instance, or None if an error occurs.
        """
        try:
            if self.config["browser"] == "chrome":
                self._driver = webdriver.Chrome()
            elif self.config["browser"] == "firefox":
                self._driver = webdriver.Firefox()
            else:
                print("Browser type not supported")
                return None
            self._driver.get(url)
            return self._driver
        except C.webDriverException as e:
            print("ERROR : ", e)
            return None