import pytest
from selenium import webdriver
from utils.config_util import ConfigUtil
# from my_pages.my_pages import LoginPage
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(params=ConfigUtil.get_browsers())
def get_browser(request):
    driver = None
    if request.param == 'chrome':
        # options = ChromeOptions()
        # options.browser_version = 'latest'
        # options.platform_name = 'Windows 11'
        # sauce_options = {}
        # sauce_options['username'] = 'oauth-lokeshreddydevireddy-f3dab'
        # sauce_options['accessKey'] = '35bd94bd-0b74-4acf-a1ff-264ce0d65cf6'
        # sauce_options['build'] = 'selenium-build-WP4M7'
        # sauce_options['name'] = '<your test name>'
        # options.set_capability('sauce:options', sauce_options)
        # url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"
        # driver = webdriver.Remote(command_executor=url, options=options)
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

