import pytest
from .fixtures_for_test import setup_and_teardown_fixture_for_getting_dashboard
from my_pages.my_pages import LoginPage, DashboardPage



@pytest.mark.logout
@pytest.mark.menu
@pytest.mark.positive
def test_logout_feature_in_dashboard(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard = setup_and_teardown_fixture_for_getting_dashboard
    current_page = dashboard.get_menu().logout()
    assert type(current_page) is LoginPage


@pytest.mark.positive
@pytest.mark.menu
def test_logout_feature_in_cart_page(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard = setup_and_teardown_fixture_for_getting_dashboard
    cart_page = dashboard.get_cart().get_cart_page()
    current_page = cart_page.get_menu().logout()
    assert type(current_page) is LoginPage


@pytest.mark.positive
@pytest.mark.menu
def test_logout_feature_in_checkout_page(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard = setup_and_teardown_fixture_for_getting_dashboard
    checkout_page = (dashboard
                     .get_cart()
                     .get_cart_page()
                     .continue_to_checkout())
    current_page = checkout_page.get_menu().logout()
    assert type(current_page) is LoginPage


@pytest.mark.positive
@pytest.mark.menu
def test_get_all_products_feature_in_cart_page(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard = setup_and_teardown_fixture_for_getting_dashboard
    cart_page = (dashboard
                 .get_cart()
                 .get_cart_page())
    current_page = cart_page.get_menu().get_all_items()
    assert type(current_page) is DashboardPage


@pytest.mark.positive
@pytest.mark.menu
def test_get_all_products_feature_in_checkout_page(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard = setup_and_teardown_fixture_for_getting_dashboard
    checkout_page = (dashboard
                     .get_cart()
                     .get_cart_page()
                     .continue_to_checkout())
    current_page = checkout_page.get_menu().get_all_items()
    assert type(current_page) is DashboardPage


@pytest.mark.positive
@pytest.mark.menu
def test_reset_app_in_cart_page(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard = setup_and_teardown_fixture_for_getting_dashboard
    cart_page = (dashboard
                 .add_backpack_to_cart()
                 .get_cart()
                 .get_cart_page())
    list_of_products_in_cart = cart_page.get_list_of_products_in_cart()
    assert len(list_of_products_in_cart) == 1
    cart_page.get_menu().reset_app()
    list_of_products_in_cart = cart_page.get_list_of_products_in_cart()
    assert len(list_of_products_in_cart) == 0


@pytest.mark.positive
@pytest.mark.menu
def test_reset_behavior_in_cart(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard = setup_and_teardown_fixture_for_getting_dashboard
    cart = (dashboard
            .add_backpack_to_cart()
            .get_cart())
    no_of_products_in_cart = cart.get_no_of_products_in_cart()
    assert no_of_products_in_cart == 1
    cart.get_cart_page().get_menu().reset_app()
    no_of_products_in_cart = cart.get_no_of_products_in_cart()
    assert no_of_products_in_cart == 0
