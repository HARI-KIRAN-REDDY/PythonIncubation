from selenium import webdriver
from config import BROWSER, USER_NAME, PASSWORD
from my_constants.pages_constants import LOGIN_PAGE_URL
from my_pages.my_pages import LoginPage


def get_browser():
    driver = None
    if BROWSER == 'chrome':
        driver = webdriver.Chrome()
    elif BROWSER == 'edge':
        driver = webdriver.Edge()
    elif BROWSER == 'firefox':
        driver = webdriver.Firefox()
    return driver


def login_and_get_dashboard(driver):
    driver.get(LOGIN_PAGE_URL)
    login_page = LoginPage(driver)
    dashboard_page = (login_page
                      .enter_user_name(USER_NAME)
                      .enter_password(PASSWORD)
                      .click_login_button())
    return dashboard_page


