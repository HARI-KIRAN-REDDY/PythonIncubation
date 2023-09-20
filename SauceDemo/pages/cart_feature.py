from selenium import webdriver
from selenium.webdriver.common.by import By
# from cart_page import CartPage


class CartFeature:
    def __init__(self, driver):
        self.__driver = driver
        self.__cart = self.__driver.find_element(By.ID, 'shopping_cart_container')

    # def get_cart(self):
    #     self.__cart.click()
    #     return CartPage(self.__driver)