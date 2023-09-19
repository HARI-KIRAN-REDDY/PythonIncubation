from abc import ABC
from selenium import webdriver
from selenium.webdriver.common.by import By
#from cart_page import CartPage
#from login_page import LoginPage


class MenuArea(ABC):
    def __init__(self, driver=webdriver.Chrome):
        self.__driver = driver
        self.__menu_area = self.__driver.find_element(By.XPATH, '//*[@id="menu_button_container"]/div/div[2]')
        self.__menu_button = self.__driver.find_element(By.ID, 'react-burger-menu-btn')
        self.__all_items_link = self.__driver.find_element(By.ID, 'inventory_sidebar_link')
        self.__menu_close_button = self.__driver.find_element(By.ID, 'react-burger-cross-btn')
        self.__logout_link = self.__driver.find_element(By.ID, 'logout_sidebar_link')

    def logout(self):
        self.__logout_link.click()
        #return LoginPage(self.__driver)



class Cart(ABC):
    def __init__(self, driver: webdriver):
        self.__driver = driver
        self.__cart = self.__driver.find_element(By.ID, 'shopping_cart_container')

    def go_to_cart(self):
        self.__cart.click()
        #return CartPage(self.__driver)
