import pytest
from exceptions.page_exceptions import InvalidCredentialsException
from utils.test_util import get_browser
# from my_pages.my_pages import LoginPage, DashboardPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.test_data_util import TestDataGetter

class TestLoginFeature:
    valid_credentials = TestDataGetter.get_valid_login_credentials()
    invalid_credentials = TestDataGetter.get_invalid_login_credentials()

    @pytest.fixture(scope='function')
    def get_login_page(self, get_browser):
        driver = get_browser
        driver.get('https:saucedemo.com')
        login_page = LoginPage(driver)
        yield login_page
        driver.close()
        driver.quit()

    @pytest.mark.parametrize('credentials', invalid_credentials)
    @pytest.mark.login
    @pytest.mark.negative
    def test_login_with_invalid_credentials(self, get_login_page, credentials):
        """Tests with invalid credentials"""
        login_page = get_login_page
        with pytest.raises(InvalidCredentialsException):
            (login_page
             .enter_user_name(credentials['user_name'])
             .enter_password(credentials['password'])
             .click_login_button())

    @pytest.mark.parametrize('credentials', valid_credentials)
    @pytest.mark.login
    @pytest.mark.positive
    def test_login_with_valid_credentials(self, get_login_page, credentials):
        """Tests with valid credentials"""
        login_page = get_login_page
        page = (login_page
                .enter_user_name(credentials['user_name'])
                .enter_password(credentials['password'])
                .click_login_button())
        assert type(page) is DashboardPage
