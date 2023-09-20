from selenium import webdriver
from selenium.webdriver.common.by import By
from dashboard_page import DashboardPage
from checkout_page import CheckoutPageOne
from .cart_feature import CartFeature
from .menu_feature import MenuFeature


class CartPage:
    def __init__(self, driver=webdriver.Chrome):
        self.__cart_feature = CartFeature(driver)
        self.__menu_feature = MenuFeature(driver)
        self.__driver = driver
        self.__continue_to_shopping_btn = self.__driver.find_element(By.ID, 'continue-shopping')
        self.__continue_to_checkout_btn = self.__driver.find_element(By.ID, 'checkout')

    def continue_to_shop(self):
        self.__continue_to_shopping_btn.click()
        return DashboardPage(self.__driver)

    def continue_to_checkout(self):
        self.__continue_to_checkout_btn.click()
        return CheckoutPageOne(self.__driver)

    def get_menu(self):
        return self.__menu_feature.get_menu_feature()
