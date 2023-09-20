from selenium.webdriver.common.by import By
from selenium import webdriver
from exceptions.page_exceptions import InvalidCredentialsException
from my_constants.pages_constants import DASHBOARD_PAGE_URL
from .dashboard_page import DashboardPage


class LoginPage:
    def __init__(self, driver: webdriver):
        self.__driver = driver
        self.__user_name_box = self.__driver.find_element(By.ID, 'user-name')
        self.__password_box = self.__driver.find_element(By.ID, 'password')
        self.__login_button = self.__driver.find_element(By.ID, 'login-button')

    def enter_user_name(self, user_name: str):
        self.__user_name_box.send_keys(user_name)
        return LoginPage(self.__driver)

    def enter_password(self, password: str):
        self.__password_box.send_keys(password)
        return LoginPage(self.__driver)

    def click_login_button(self):
        self.__login_button.click()
        if self.__driver.current_url == DASHBOARD_PAGE_URL:
            return DashboardPage(self.__driver)
        else:
            raise InvalidCredentialsException('Invalid Credentials Entered, Check your input')
