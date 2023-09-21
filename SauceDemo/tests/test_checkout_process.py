import pytest
from my_pages.my_pages import CheckoutCompletePage
from .fixtures_for_test import setup_and_teardown_fixture_for_getting_dashboard
from exceptions.page_exceptions import IncompleteDetailsException


@pytest.mark.negative
def test_checkout_process_with_empty_cart_and_without_giving_details(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard = setup_and_teardown_fixture_for_getting_dashboard
    checkout_page = (dashboard
                     .get_cart()
                     .get_cart_page()
                     .continue_to_checkout())
    try:
        (checkout_page
         .continue_to_final_step_in_checkout())
    except Exception as expected_exception:
        assert type(expected_exception) is IncompleteDetailsException


@pytest.mark.parametrize('first_name, last_name, zipcode',[('John', 'Wick', 1234)])
@pytest.mark.positive
def test_checkout_process_with_empty_cart_and_by_giving_details(setup_and_teardown_fixture_for_getting_dashboard, first_name, last_name, zipcode):
    dashboard = setup_and_teardown_fixture_for_getting_dashboard
    current_page = (dashboard
                    .get_cart()
                    .get_cart_page()
                    .continue_to_checkout()
                    .enter_first_name(first_name)
                    .enter_last_name(last_name)
                    .enter_zipcode(zipcode)
                    .continue_to_final_step_in_checkout()
                    .confirm_order())
    assert type(current_page) is CheckoutCompletePage

