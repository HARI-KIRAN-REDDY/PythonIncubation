from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class MenuFeature:
    def __init__(self, driver):
        self.__driver = driver
        self.__menu_area = self.__driver.find_element(By.XPATH, '//*[@id="menu_button_container"]/div/div[2]')
        self.__menu_button = self.__driver.find_element(By.ID, 'react-burger-menu-btn')
        self.__all_items_link = self.__driver.find_element(By.ID, 'inventory_sidebar_link')
        self.__menu_close_button = self.__driver.find_element(By.ID, 'react-burger-cross-btn')
        self.__logout_link = self.__driver.find_element(By.ID, 'logout_sidebar_link')
        self.__reset_app_link = self.__driver.find_element(By.ID, 'reset_sidebar_link')
        self.__wait = WebDriverWait(driver, 10)

    def get_all_items(self):
        if self.__menu_area.get_attribute('aria-hidden') == 'true':
            self.__menu_button.click()
        self.__wait.until(EC.element_to_be_clickable(self.__all_items_link))
        self.__all_items_link.click()
        from pages.dashboard_page import DashboardPage
        return DashboardPage(self.__driver)

    def get_menu_feature(self):
        if self.__menu_area.get_attribute('aria-hidden') == 'true':
            self.__menu_button.click()
        return MenuFeature(self.__driver)

    def reset_app(self):
        if self.__menu_area.get_attribute('aria-hidden') == 'true':
            self.__menu_button.click()
        self.__wait.until(EC.element_to_be_clickable(self.__reset_app_link))
        self.__reset_app_link.click()
        return MenuFeature(self.__driver)

    def logout(self):
        if self.__menu_area.get_attribute('aria-hidden') == 'true':
            self.__menu_button.click()
        self.__wait.until(EC.element_to_be_clickable(self.__logout_link))
        self.__logout_link.click()
        from pages.login_page import LoginPage
        return LoginPage(self.__driver)
