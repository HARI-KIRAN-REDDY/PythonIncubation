import pytest
from my_pages.my_pages import *


@pytest.mark.parametrize('user_name, password', [('standard_user', 'secret_sauce'),
                                                 ('locked_out_user', 'secret_sauce'),
                                                 ('problem_user', 'secret_sauce')])
def test_login_with_valid_credentials(setup_and_teardown_fixture_for_login, user_name, password):
    "Tests with valid credentials"
    login_page = setup_and_teardown_fixture_for_login
    page = (login_page
            .enter_user_name(user_name)
            .enter_password(password)
            .click_login_button())
    assert type(page) is DashboardPage

@pytest.mark.parametrize('user_name, password', [('', 'empty_user_wrong_password'),
                                                 ('empty_password_wrong_user', ''),
                                                 ('', ''),
                                                 ('wrong_user_name', 'wrong_password')])
def test_login_with_invalid_credentials(setup_and_teardown_fixture_for_login, user_name, password):
    "Tests with invalid credentials"
    login_page = setup_and_teardown_fixture_for_login
    with pytest.raises(InvalidCredentialsException):
        (login_page
         .enter_user_name(user_name)
         .enter_password(password)
         .click_login_button())


def test_login_wi(setup_and_teardown_fixture):
    "Tests with invalid credential"
    login_page = setup_and_teardown_fixture
    dash_board_page = (login_page.enter_user_name('standard_user')
                       .enter_password('secret_sauce')
                       .click_login_button()
                       .add_backpack_to_cart()
                       .add_bike_light_to_cart())
    print('Number of products are', dash_board_page.get_cart().get_no_of_products_in_cart())

