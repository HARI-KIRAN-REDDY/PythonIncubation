import pytest
from my_pages.my_pages import *
from .fixtures_for_test import setup_and_teardown_fixture_for_login
from .data_providing_fixtures_for_test import get_invalid_login_credentials, get_valid_login_credentials



@pytest.mark.parametrize('user_name, password', [('standard_user', 'secret_sauce'),
                                                 ('locked_out_user', 'secret_sauce'),
                                                 ('problem_user', 'secret_sauce')])
@pytest.mark.login
@pytest.mark.positive
def test_login_with_valid_credentials(setup_and_teardown_fixture_for_login, get_valid_login_credentials):
    user_name, password = get_valid_login_credentials
    """Tests with valid credentials"""
    login_page = setup_and_teardown_fixture_for_login
    page = (login_page
            .enter_user_name(user_name)
            .enter_password(password)
            .click_login_button())
    assert type(page) is DashboardPage


@pytest.mark.parametrize('user_name, password', [('a','b')])
@pytest.mark.login
@pytest.mark.negative
def test_login_with_invalid_credentials(setup_and_teardown_fixture_for_login, user_name, password):
    """Tests with invalid credentials"""
    login_page = setup_and_teardown_fixture_for_login
    with pytest.raises(InvalidCredentialsException):
        (login_page
         .enter_user_name(user_name)
         .enter_password(password)
         .click_login_button())
