import pytest
from exceptions.page_exceptions import InvalidCredentialsException
from .test_utils import get_browser
from my_pages.my_pages import LoginPage, DashboardPage
from my_constants.pages_constants import LOGIN_PAGE_URL
class TestLoginFeature:

    @pytest.fixture(scope='function')
    def get_login_page(self):
        driver = get_browser()
        driver.get(LOGIN_PAGE_URL)
        login_page = LoginPage(driver)
        yield login_page
        driver.close()
        driver.quit()

    @pytest.mark.parametrize('user_name, password', [('', 'empty_user_wrong_password'),
                                                     ('empty_password_wrong_user', ''),
                                                     ('', ''),
                                                     ('wrong_user_name', 'wrong_password')])
    @pytest.mark.login
    @pytest.mark.negative
    def test_login_with_invalid_credentials(self, get_login_page, user_name, password):
        """Tests with invalid credentials"""
        login_page = get_login_page
        with pytest.raises(InvalidCredentialsException):
            (login_page
             .enter_user_name(user_name)
             .enter_password(password)
             .click_login_button())


    @pytest.mark.parametrize('user_name, password', [('standard_user', 'secret_sauce'),
                                                     ('locked_out_user', 'secret_sauce'),
                                                     ('problem_user', 'secret_sauce')])
    @pytest.mark.login
    @pytest.mark.positive
    def test_login_with_valid_credentials(self, get_login_page, user_name, password):
        """Tests with valid credentials"""
        login_page = get_login_page
        page = (login_page
                .enter_user_name(user_name)
                .enter_password(password)
                .click_login_button())
        assert type(page) is DashboardPage