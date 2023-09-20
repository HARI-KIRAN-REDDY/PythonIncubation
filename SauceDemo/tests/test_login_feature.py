import pytest
from my_pages.my_pages import *


@pytest.fixture(scope='function')
def setup_and_teardown_fixture():
    driver = webdriver.Chrome()
    driver.get(LOGIN_PAGE_URL)
    login_page = LoginPage(driver)
    yield login_page
    driver.quit()


@pytest.mark.parametrize('user_name, password', [('standard_user', 'secret_sauce'),
                                                 ('locked_out_user', 'secret_sauce'),
                                                 ('problem_user', 'secret_sauce')])
def test_login_with_valid_credentials(setup_and_teardown_fixture, user_name, password):
    login_page = setup_and_teardown_fixture
    page = (login_page
            .enter_user_name(user_name)
            .enter_password(password)
            .click_login_button())
    assert type(page) is DashboardPage
