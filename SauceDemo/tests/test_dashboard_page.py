import pytest

from .fixtures_for_test import setup_and_teardown_fixture_for_getting_dashboard


@pytest.mark.dashboard
@pytest.mark.positive
def test_product_sort_container_sort_name_wise_a_to_z(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard_page = setup_and_teardown_fixture_for_getting_dashboard
    '''first we will store list of available products, then we will sort(a to z) 
    and also we will sort dashboard to compare or to assert'''
    list_of_products_available_in_dashboard_page = dashboard_page.get_list_of_available_products_on_dashboard()
    list_of_products_sorted_a_to_z = sorted(list_of_products_available_in_dashboard_page)
    dashboard_page = dashboard_page.sort_products_by_name_a_to_z()
    assert dashboard_page.get_list_of_available_products_on_dashboard() == list_of_products_sorted_a_to_z

@pytest.mark.dashboard
@pytest.mark.positive
def test_product_sort_container_sort_name_wise_z_to_a(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard_page = setup_and_teardown_fixture_for_getting_dashboard
    '''first we will store list of available products, then we will sort(z to a) 
        and also we will sort dashboard to compare or to assert'''
    list_of_products_available_in_dashboard_page = dashboard_page.get_list_of_available_products_on_dashboard()
    list_of_products_sorted_a_to_z = sorted(list_of_products_available_in_dashboard_page, reverse=True)
    dashboard_page = dashboard_page.sort_products_by_name_z_to_a()
    assert dashboard_page.get_list_of_available_products_on_dashboard() == list_of_products_sorted_a_to_z