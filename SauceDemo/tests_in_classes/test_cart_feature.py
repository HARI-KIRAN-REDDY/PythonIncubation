import pytest
from utils.test_util import get_browser
from utils.config_util import ConfigUtil
from my_pages.my_pages import LoginPage


class TestCart:
    @pytest.fixture(scope='function')
    def get_cart_feature(self, get_browser):
        driver = get_browser
        driver.get(ConfigUtil.get_login_page_url())
        login_page = LoginPage(driver)
        cart = (login_page
                .enter_user_name(ConfigUtil.get_user_name())
                .enter_password(ConfigUtil.get_password())
                .click_login_button()
                .get_cart())
        yield cart
        driver.quit()

    @pytest.mark.cart
    @pytest.mark.positive
    def test_adding_products_to_cart(self, get_cart_feature):
        cart = get_cart_feature
        cart = (cart
                .get_cart_page()
                .continue_to_shop()
                .add_backpack_to_cart()
                .add_bike_light_to_cart()
                .get_cart())
        assert cart.get_no_of_products_in_cart() == 2

    @pytest.mark.cart_page
    @pytest.mark.positive
    def test_added_products_displayed_in_cart_page(self, get_cart_feature):
        cart = get_cart_feature
        cart_page = (cart
                     .get_cart_page()
                     .continue_to_shop()
                     .add_backpack_to_cart()
                     .add_bike_light_to_cart()
                     .get_cart()
                     .get_cart_page())
        list_of_products_displayed = cart_page.get_list_of_products_in_cart()
        print(f'Products added to cart {list_of_products_displayed}')
        assert not len(list_of_products_displayed) == 0

    @pytest.mark.cart
    @pytest.mark.dashboard
    @pytest.mark.positive
    def test_removing_products_from_cart_in_dashboard_page(self, get_cart_feature):
        cart = get_cart_feature
        cart = (cart
                .get_cart_page()
                .continue_to_shop()
                .add_backpack_to_cart()
                .add_bike_light_to_cart()
                .get_cart())
        assert cart.get_no_of_products_in_cart() == 2
        dashboard_page = (cart
                          .get_cart_page()
                          .continue_to_shop())
        cart = (dashboard_page
                .remove_backpack_from_cart()
                .remove_bike_light_from_cart()
                .get_cart())
        assert cart.get_no_of_products_in_cart() == 0
