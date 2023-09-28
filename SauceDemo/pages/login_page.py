from selenium.webdriver.common.by import By
from utils.config_util import ConfigUtil
from exceptions.page_exceptions import InvalidCredentialsException
from .dashboard_page import DashboardPage


class LoginPage:
    def __init__(self, driver):
        self.__driver = driver
        self.__user_name_box = self.__driver.find_element(By.ID, 'user-name')
        self.__password_box = self.__driver.find_element(By.ID, 'password')
        self.__login_button = self.__driver.find_element(By.ID, 'login-button')
        self.__error_element = self.__driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')

    def enter_user_name(self, user_name: str):
        self.__user_name_box.send_keys(user_name)
        return LoginPage(self.__driver)

    def enter_password(self, password: str):
        self.__password_box.send_keys(password)
        return LoginPage(self.__driver)

    def click_login_button(self):
        self.__login_button.click()
        if self.__driver.current_url == ConfigUtil.get_dashboard_page_url():
            return DashboardPage(self.__driver)
        else:
            error_message = self.__error_element.text
            raise InvalidCredentialsException(error_message)
