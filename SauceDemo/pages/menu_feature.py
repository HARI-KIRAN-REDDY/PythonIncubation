from selenium import webdriver
from selenium.webdriver.common.by import By
# from login_page import LoginPage
# from dashboard_page import DashboardPage


class MenuFeature:
    def __init__(self, driver=webdriver.Chrome()):
        self.__driver = driver
        self.__menu_area = self.__driver.find_element(By.XPATH, '//*[@id="menu_button_container"]/div/div[2]')
        self.__menu_button = self.__driver.find_element(By.ID, 'react-burger-menu-btn')
        self.__all_items_link = self.__driver.find_element(By.ID, 'inventory_sidebar_link')
        self.__menu_close_button = self.__driver.find_element(By.ID, 'react-burger-cross-btn')
        self.__logout_link = self.__driver.find_element(By.ID, 'logout_sidebar_link')
        self.__menu_button.click()

    # def get_all_items(self):
    #     if not self.__menu_area.is_displayed():
    #         self.__menu_button.click()
    #     self.__all_items_link.click()
    #     return DashboardPage(self.__driver)

    def get_menu_feature(self):
        if not self.__menu_area.is_displayed():
            self.__menu_button.click()
        return MenuFeature(self.__driver)

    # def logout(self):
    #     if not self.__menu_area.is_displayed():
    #         self.__menu_button.click()
    #     self.__logout_link.click()
    #     return LoginPage(self.__driver)
