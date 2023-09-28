from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.config_util import ConfigUtil
from pages.common_feature import Cart, Menu
from pages.cart_feature import CartFeature
from pages.menu_feature import MenuFeature


class DashboardPage(Cart, Menu):
    def __init__(self, driver):
        self.__cart_feature = CartFeature.get_cart(driver)
        self.__menu_feature = MenuFeature(driver)
        self.__driver = driver
        self.__product_sorting_select_container = Select(
            self.__driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select'))
        self.__backpack_product_button = self.__driver.find_element(By.CSS_SELECTOR, '[id*="backpack"]')
        self.__bike_light_product_button = self.__driver.find_element(By.CSS_SELECTOR, '[id*="bike-light"]')
        self.__list_of_available_products_on_dashboard = self.__driver.find_elements(By.XPATH,
                                                                                     '//div[@class = "inventory_item"]//a/div')

    def sort_products_by_price(self):
        self.__product_sorting_select_container.select_by_index(2)
        return DashboardPage(self.__driver)

    def sort_products_by_name_a_to_z(self):
        self.__product_sorting_select_container.select_by_index(0)
        return DashboardPage(self.__driver)

    def sort_products_by_name_z_to_a(self):
        self.__product_sorting_select_container.select_by_index(1)
        return DashboardPage(self.__driver)

    def get_list_of_available_products_on_dashboard(self):
        return [product.text for product in self.__list_of_available_products_on_dashboard]

    def add_backpack_to_cart(self):
        if self.__backpack_product_button.text == 'Add to cart':
            self.__cart_feature.add_product_to_cart(ConfigUtil.get_backpack_product_name())
            self.__backpack_product_button.click()
        return DashboardPage(self.__driver)

    def remove_backpack_from_cart(self):
        if self.__backpack_product_button.text == 'Remove':
            self.__backpack_product_button.click()
            self.__cart_feature.remove_product_from_cart(ConfigUtil.get_backpack_product_name())
        return DashboardPage(self.__driver)

    def add_bike_light_to_cart(self):
        if self.__bike_light_product_button.text == 'Add to cart':
            self.__cart_feature.add_product_to_cart(ConfigUtil.get_bike_light_product_name())
            self.__bike_light_product_button.click()
        return DashboardPage(self.__driver)

    def remove_bike_light_from_cart(self):
        if self.__bike_light_product_button.text == 'Remove':
            self.__bike_light_product_button.click()
            self.__cart_feature.remove_product_from_cart(ConfigUtil.get_bike_light_product_name())
        return DashboardPage(self.__driver)

    def get_menu(self):
        return self.__menu_feature.get_menu_feature()

    def get_cart(self):
        return self.__cart_feature.get_cart(self.__driver)
