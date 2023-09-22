import pytest
from my_constants.pages_constants import LOGIN_PAGE_URL
from config import USER_NAME, PASSWORD
from my_pages.my_pages import LoginPage
from .test_utils import get_browser, login_and_get_dashboard


class TestDashboard:
    @pytest.fixture(scope='function')
    def get_dashboard(self):
        driver = get_browser()
        dashboard_page = login_and_get_dashboard(driver)
        yield dashboard_page
        driver.quit()

    @pytest.mark.dashboard
    @pytest.mark.positive
    def test_product_sort_container_sort_name_wise_a_to_z(self, get_dashboard):
        dashboard_page = get_dashboard
        '''first we will store list of available products, then we will sort(a to z) 
        and also we will sort dashboard to compare or to assert'''
        list_of_products_available_in_dashboard_page = dashboard_page.get_list_of_available_products_on_dashboard()
        list_of_products_sorted_a_to_z = sorted(list_of_products_available_in_dashboard_page)
        dashboard_page = dashboard_page.sort_products_by_name_a_to_z()
        assert dashboard_page.get_list_of_available_products_on_dashboard() == list_of_products_sorted_a_to_z

    @pytest.mark.dashboard
    @pytest.mark.positive
    def test_product_sort_container_sort_name_wise_z_to_a(self, get_dashboard):
        dashboard_page = get_dashboard
        '''first we will store list of available products, then we will sort(z to a) 
            and also we will sort dashboard to compare or to assert'''
        list_of_products_available_in_dashboard_page = dashboard_page.get_list_of_available_products_on_dashboard()
        list_of_products_sorted_a_to_z = sorted(list_of_products_available_in_dashboard_page, reverse=True)
        dashboard_page = dashboard_page.sort_products_by_name_z_to_a()
        assert dashboard_page.get_list_of_available_products_on_dashboard() == list_of_products_sorted_a_to_z
