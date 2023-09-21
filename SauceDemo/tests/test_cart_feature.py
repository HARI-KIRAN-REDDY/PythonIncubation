from .fixtures_for_test import setup_and_teardown_fixture_for_getting_dashboard


def test_adding_products_to_cart(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard_page = setup_and_teardown_fixture_for_getting_dashboard
    cart = (dashboard_page
            .add_backpack_to_cart()
            .add_bike_light_to_cart()
            .get_cart())
    assert cart.get_no_of_products_in_cart() == 2


def test_added_products_displayed_in_cart_page(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard_page = setup_and_teardown_fixture_for_getting_dashboard
    cart_page = (dashboard_page
                 .add_backpack_to_cart()
                 .add_bike_light_to_cart()
                 .get_cart()
                 .get_cart_page())
    list_of_products_displayed = cart_page.get_list_of_products_in_cart()
    print(f'Products added to cart {list_of_products_displayed}')
    assert not len(list_of_products_displayed) == 0


def test_removing_products_from_cart_in_dashboard_page(setup_and_teardown_fixture_for_getting_dashboard):
    dashboard_page = setup_and_teardown_fixture_for_getting_dashboard
    cart = (dashboard_page
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
