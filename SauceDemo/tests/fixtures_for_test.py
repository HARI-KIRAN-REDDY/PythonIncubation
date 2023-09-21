import pytest
from my_constants.pages_constants import LOGIN_PAGE_URL
from config import BROWSER, USER_NAME, PASSWORD
from my_pages.my_pages import *


@pytest.fixture(scope='function')
def setup_and_teardown_fixture_for_login():
    driver = get_browser()
    driver.get(LOGIN_PAGE_URL)
    login_page = LoginPage(driver)
    yield login_page
    driver.quit()


@pytest.fixture(scope='function')
def setup_and_teardown_fixture_for_getting_dashboard():
    driver = get_browser()
    dashboard_page = login(driver)
    yield dashboard_page
    logout(driver)
    driver.quit()


def login(driver):
    driver.get(LOGIN_PAGE_URL)
    login_page = LoginPage(driver)
    dash_board_page = login_page.enter_user_name(USER_NAME).enter_password(PASSWORD).click_login_button()
    return dash_board_page


def logout(driver):
    pass


def get_browser():
    driver = None
    if BROWSER == 'chrome':
        driver = webdriver.Chrome()
    elif BROWSER == 'edge':
        driver = webdriver.Edge()
    elif BROWSER == 'firefox':
        driver = webdriver.Firefox()
    return driver
