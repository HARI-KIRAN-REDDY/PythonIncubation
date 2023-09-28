from selenium.webdriver.common.by import By
from .common_feature import Cart, Menu
from .cart_feature import CartFeature
from .menu_feature import MenuFeature
from .dashboard_page import DashboardPage
from .checkout_page import CheckoutPageOne
from exceptions.page_exceptions import ZeroProductsInCartException


class CartPage(Cart, Menu):
    def __init__(self, driver):
        self.__cart_feature = CartFeature.get_cart(driver)
        self.__menu_feature = MenuFeature(driver)
        self.__driver = driver
        self.__continue_to_shopping_btn = self.__driver.find_element(By.ID, 'continue-shopping')
        self.__continue_to_checkout_btn = self.__driver.find_element(By.ID, 'checkout')
        try:
            self.__list_of_products = self.__driver.find_elements(By.XPATH,
                                                                  '//div[@class="cart_list"]//a/div[@class="inventory_item_name"]')
        except ZeroProductsInCartException as e:
            print(f'Warning, no products in cart')

    def continue_to_shop(self):
        self.__continue_to_shopping_btn.click()
        return DashboardPage(self.__driver)

    def continue_to_checkout(self):
        self.__continue_to_checkout_btn.click()
        return CheckoutPageOne(self.__driver)

    def get_list_of_products_in_cart(self):
        return [product.text for product in self.__list_of_products]

    def get_cart(self):
        return self.__cart_feature.get_cart(self.__driver)

    def get_menu(self):
        return self.__menu_feature.get_menu_feature()
