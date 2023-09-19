from selenium import webdriver
from selenium.webdriver.common.by import By

from common_feature import MenuArea, Cart
from selenium.webdriver.support.ui import Select
from time import sleep


class DashboardPage(MenuArea, Cart):
    def __init__(self, driver: webdriver):
        MenuArea.__init__(self, driver)
        Cart.__init__(self, driver)
        self.__driver = driver
        self.__product_sorting_select_container = Select(
            self.__driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select'))
        self.__backpack_product_button = self.__driver.find_element(By.CSS_SELECTOR, '[id*="backpack"]')
        self.__bike_light_product_button = self.__driver.find_element(By.CSS_SELECTOR, '[id*="bike-light"]')

    def sort_products_by_price(self):
        self.__product_sorting_select_container.select_by_index(2)
        return DashboardPage(self.__driver)

    def sort_products_by_name(self):
        self.__product_sorting_select_container.select_by_index(0)
        return DashboardPage(self.__driver)

    def add_backpack_to_cart(self):
        sleep(3)
        self.__backpack_product_button.click()
        sleep(3)
        return DashboardPage(self.__driver)

    def add_bike_light_to_cart(self):
        self.__bike_light_product_button.click()
        return DashboardPage(self.__driver)
