from common_feature import MenuArea, Cart
from selenium import webdriver
from selenium.webdriver.common.by import By
from dashboard_page import DashboardPage


class CheckoutCompletePage(MenuArea, Cart):
    def __init__(self, driver: webdriver):
        MenuArea.__init__(self, driver)
        Cart.__init__(self, driver)
        self.__driver = driver
        self.__back_to_home_btn = self.__driver.find_element(By.ID, 'back-to-products')

    def back_to_dashboard(self):
        self.__back_to_home_btn.click()
        return DashboardPage(self.__driver)