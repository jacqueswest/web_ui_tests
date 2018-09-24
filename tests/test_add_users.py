import pytest
from json import load
from lib.driver import WebDriver
from page_objects.add_user import add_user
import selenium.webdriver.chrome.service as s
from page_objects.landing_page import verify_landing_on_table_list


@pytest.fixture(scope="module")
def env_setup(data_setup):
    global driver

    env_data = data.get("locator_data")
    chrome_path = env_data.get("chrome_path")
    url = env_data.get("url")

    service = s.Service('./chromedriver')
    service.start()
    capabilities = {'chrome.binary': chrome_path}
    driver = WebDriver(command_executor=service.service_url, desired_capabilities=capabilities)
    driver.set_window_size(1920, 1080)
    driver.get(url)
    yield
    driver.close()


@pytest.fixture(scope="module")
def data_setup():
    global data

    with open(file="./test_data_lib/user_data.json") as f:
        data = load(f)


def test_verify_landing_on_user_list_table(env_setup, data_setup):
    """ Verify landing on user list table """

    result = verify_landing_on_table_list(browser=driver, locators=data.get("locator_data"))
    assert result is True


def test_can_add_user_one(env_setup, data_setup):
    """ Can add user1 """

    results = add_user(browser=driver, user="user1", **data)
    assert results == "Add PASSED"


def test_can_add_user_two(env_setup, data_setup):
    """ Can add user2 """

    results = add_user(browser=driver, user="user2", **data)
    assert results == "Add PASSED"
