import pytest
from selenium import webdriver
from utils.config_util import ConfigUtil
from my_pages.my_pages import LoginPage


@pytest.fixture(params=ConfigUtil.get_browsers())
def get_browser(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'edge':
        driver = webdriver.Edge()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    return driver


def login_and_get_dashboard(driver):
    driver.get(ConfigUtil.get_login_page_url())
    login_page = LoginPage(driver)
    dashboard_page = (login_page
                      .enter_user_name(ConfigUtil.get_user_name())
                      .enter_password(ConfigUtil.get_password())
                      .click_login_button())
    return dashboard_page

