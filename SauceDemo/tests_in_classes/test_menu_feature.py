import pytest
from my_pages.my_pages import LoginPage
from utils.test_util import get_browser, login_and_get_dashboard


class TestMenu:
    @pytest.fixture(scope='function')
    def get_dashboard(self, get_browser):
        driver = get_browser
        dashboard_page = login_and_get_dashboard(driver)
        yield dashboard_page
        driver.quit()


    @pytest.mark.logout
    @pytest.mark.menu
    @pytest.mark.positive
    def test_logout_feature_in_dashboard(self, get_dashboard):
        dashboard = get_dashboard
        current_page = dashboard.get_menu().logout()
        assert type(current_page) is LoginPage

    @pytest.mark.positive
    @pytest.mark.menu
    def test_logout_feature_in_cart_page(self, get_dashboard):
        dashboard = get_dashboard
        cart_page = dashboard.get_cart().get_cart_page()
        current_page = cart_page.get_menu().logout()
        assert type(current_page) is LoginPage

    @pytest.mark.positive
    @pytest.mark.menu
    def test_logout_feature_in_checkout_page(self, get_dashboard):
        dashboard = get_dashboard
        checkout_page = (dashboard
                         .get_cart()
                         .get_cart_page()
                         .continue_to_checkout())
        current_page = checkout_page.get_menu().logout()
        assert type(current_page) is LoginPage
