import pytest
from json import load
from lib.driver import WebDriver
from page_objects.add_user import Actions as AddUserActions
import selenium.webdriver.chrome.service as s
from page_objects.landing_page import Actions as LandingPageActions
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def env_setup():
    global driver

    chrome_path = "/Applications/Google Chrome.app"
    url = "http://www.way2automation.com/angularjs-protractor/webtables/"

    service = s.Service('./chromedriver')
    service.start()
    capabilities = {'chrome.binary': chrome_path}
    driver = WebDriver(command_executor=service.service_url, desired_capabilities=capabilities)
    driver.set_window_size(1920, 1080)
    driver.get(url)
    yield
    driver.close()


@pytest.fixture(scope="module")
def add_user_action():
    return AddUserActions(driver=driver)


@pytest.fixture(scope="module")
def landing_page_action():
    return LandingPageActions(driver=driver)


def test_verify_landing_on_user_list_table(env_setup, landing_page_action):
    """ Verify landing on user list table """

    result = landing_page_action.verify_landing_on_table_list()
    assert result is True


def test_can_add_user_one(env_setup, add_user_action):
    """ Can add user1 """

    results = add_user_action.add_user(user="user1")
    assert results == "Add PASSED"


def test_can_add_user_two(env_setup, add_user_action):
    """ Can add user2 """

    results = add_user_action.add_user(user="user2")
    assert results == "Add PASSED"
