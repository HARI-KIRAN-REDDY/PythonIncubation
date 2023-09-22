import pytest
from my_pages.my_pages import CheckoutCompletePage
from exceptions.page_exceptions import IncompleteDetailsException
from .test_utils import get_browser, login_and_get_dashboard


class TestCheckout:
    @pytest.fixture(scope='function')
    def get_dashboard(self):
        driver = get_browser()
        dashboard_page = login_and_get_dashboard(driver)
        yield dashboard_page
        driver.quit()

    @pytest.mark.negative
    def test_checkout_process_with_empty_cart_and_without_giving_details(self, get_dashboard):
        dashboard = get_dashboard
        checkout_page = (dashboard
                         .get_cart()
                         .get_cart_page()
                         .continue_to_checkout())
        try:
            (checkout_page
             .continue_to_final_step_in_checkout())
        except Exception as expected_exception:
            assert type(expected_exception) is IncompleteDetailsException

    @pytest.mark.parametrize('details', [
        {'first_name': 'John', 'last_name': 'Wick', 'zipcode': 1234}])
    @pytest.mark.positive
    def test_checkout_process_with_empty_cart_and_by_giving_details(self, get_dashboard, details):
        dashboard = get_dashboard
        current_page = (dashboard
                        .get_cart()
                        .get_cart_page()
                        .continue_to_checkout()
                        .enter_first_name(details['first_name'])
                        .enter_last_name(details['last_name'])
                        .enter_zipcode(details['zipcode'])
                        .continue_to_final_step_in_checkout()
                        .confirm_order())
        assert type(current_page) is CheckoutCompletePage
