from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class WebDriver(webdriver.Remote):
    """
    Minimal subclassing of webdriver, primarily to return a WebElement which has consistent _by_locator methods
    """

    def __init__(self, **kwargs):
        super(WebDriver, self).__init__(**kwargs)

    @staticmethod
    def get_locator(locator):
        try:
            locator_type, locator_value = locator
        except AttributeError as e:
            raise Exception(e)
        except ValueError as e:
            raise Exception(e)

        locator_type = getattr(By, locator_type.upper())
        return locator_type, locator_value

    def visibility_of_element(self, driver, locator, wait):
        locator_type, locator_value = self.get_locator(locator)
        try:
            element = WebDriverWait(driver, wait).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            return element
        except TimeoutException as e:
            raise Exception(e)

    def find_element_by_locator(self, locator):
        locator_type, locator_value = self.get_locator(locator)
        try:
            element = self.find_element(locator_type, locator_value)
        except AttributeError:
            raise Exception('Invalid locator: {0}'.format(locator_type))
        return element

    def find_elements_by_locator(self, locator):
        locator_type, locator_value = self.get_locator(locator)
        try:
            elements = self.find_elements(locator_type, locator_value)
        except AttributeError:
            raise Exception('Invalid locator: {0}'.format(locator_type))
        return [element for element in elements]

    def select_by_text(self, locator, text):
        select = Select(self.find_element_by_locator(locator))
        return select.select_by_visible_text(text)

    def is_element_present(self, locator):
        try:
            self.find_element_by_locator(locator)
            return True
        except NoSuchElementException:
            return False

    def is_visible(self, locator):
        if self.is_element_present(locator):
            if self.find_element_by_locator(locator).is_displayed():
                return True
            else:
                return False
        else:
            return False

    def is_element_available(self, locator):
        if self.is_visible(locator):
            return True
        else:
            return False

    def wait_for_element_is_clickable(self, driver, locator, wait):
        locator_type, locator_value = self.get_locator(locator)
        try:
            element = WebDriverWait(driver, wait).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            return element
        except TimeoutException as e:
            raise Exception(e)

    def wait_for_element_is_invisible(self, driver, locator, wait):
        locator_type, locator_value = self.get_locator(locator)
        try:
            element = WebDriverWait(driver, wait).until(
                EC.invisibility_of_element_located((locator_type, locator_value))
            )
            return element
        except TimeoutException as e:
            return False  # raise Exception(e)