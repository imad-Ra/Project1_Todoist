class BasePage:
    """
    A base class for all page objects in the application.
    This class provides common functionality that can be inherited by specific page classes.
    """

    def __init__(self, driver):
        """
        Initialize the BasePage object.
        Args:
            driver: The WebDriver instance to use for browser interactions.
        """
        self._driver = driver

    def refresh_page(self):
        """
        Refresh the current page in the browser.
        """
        self._driver.reload()