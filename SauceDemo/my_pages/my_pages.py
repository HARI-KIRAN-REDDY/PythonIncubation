from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from my_constants.pages_constants import LOGIN_PAGE_URL, DASHBOARD_PAGE_URL
from exceptions.page_exceptions import InvalidCredentialsException, IncompleteDetailsException
from time import sleep

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

class DashboardPage:
    def __init__(self, driver: webdriver):
        self.__cart_feature = CartFeature(driver)
        self.__menu_feature = MenuFeature(driver)
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

    def get_menu(self):
        return self.__menu_feature.get_menu_feature()


class CheckoutPageOne:
    def __init__(self, driver: webdriver):
        self.__cart_feature = CartFeature(driver)
        self.__menu_feature = MenuFeature(driver)
        self.__driver = driver
        self.__first_name_text_box = self.__driver.find_element(By.ID, 'first-name')
        self.__last_name_text_box = self.__driver.find_element(By.ID, 'last-name')
        self.__zipcode_text_box = self.__driver.find_element(By.ID, 'postal-code')
        self.__continue_button = self.__driver.find_element(By.ID, 'continue')

    def enter_first_name(self, first_name: str):
        self.__first_name_text_box.send_keys(first_name)
        return CheckoutPageOne(self.__driver)

    def enter_last_name(self, last_name: str):
        self.__last_name_text_box.send_keys(last_name)
        return CheckoutPageOne(self.__driver)

    def enter_zipcode(self, zipcode: int):
        self.__zipcode_text_box.send_keys(zipcode)
        return CheckoutPageOne(self.__driver)

    def continue_to_checkout(self):
        list_of_text_fields = [self.__first_name_text_box, self.__last_name_text_box, self.__zipcode_text_box]
        if not self.__is_no_field_empty(list_of_text_fields):
            raise IncompleteDetailsException('Makesure you entered first-name, last-name and zipcode fields')
        return CheckoutPageTwo(self.__driver)

    def __is_no_field_empty(self, *text_boxes):
        for text_box in text_boxes:
            if text_box.get_attribute('value') == '':
                return False
        return True

    def get_menu(self):
        return self.__menu_feature.get_menu_feature()


class CheckoutPageTwo:
    def __init__(self, driver: webdriver):
        self.__cart_feature = CartFeature(driver)
        self.__menu_feature = MenuFeature(driver)
        self.__driver = driver
        self.__finish_btn = self.__driver.find_element(By.ID, 'finish')

    def confirm_order(self):
        self.__finish_btn.click()

    def get_menu(self):
        return self.__menu_feature.get_menu_feature()



class CheckoutCompletePage:
    def __init__(self, driver: webdriver):
        self.__driver = driver
        self.__back_to_home_btn = self.__driver.find_element(By.ID, 'back-to-products')

    def back_to_dashboard(self):
        self.__back_to_home_btn.click()
        return DashboardPage(self.__driver)


class CartPage:
    def __init__(self, driver):
        self.__cart_feature = CartFeature(driver)
        self.__menu_feature = MenuFeature(driver)
        self.__driver = driver
        self.__continue_to_shopping_btn = self.__driver.find_element(By.ID, 'continue-shopping')
        self.__continue_to_checkout_btn = self.__driver.find_element(By.ID, 'checkout')

    def continue_to_shop(self):
        self.__continue_to_shopping_btn.click()
        return DashboardPage(self.__driver)


class MenuFeature:
    def __init__(self, driver):
        self.__driver = driver
        self.__menu_area = self.__driver.find_element(By.XPATH, '//*[@id="menu_button_container"]/div/div[2]')
        self.__menu_button = self.__driver.find_element(By.ID, 'react-burger-menu-btn')
        self.__all_items_link = self.__driver.find_element(By.ID, 'inventory_sidebar_link')
        self.__menu_close_button = self.__driver.find_element(By.ID, 'react-burger-cross-btn')
        self.__logout_link = self.__driver.find_element(By.ID, 'logout_sidebar_link')
        self.__menu_button.click()

    def get_all_items(self):
        if not self.__menu_area.is_displayed():
            self.__menu_button.click()
        self.__all_items_link.click()
        return DashboardPage(self.__driver)

    def get_menu_feature(self):
        if not self.__menu_area.is_displayed():
            self.__menu_button.click()
        return MenuFeature(self.__driver)

    def logout(self):
        if not self.__menu_area.is_displayed():
            self.__menu_button.click()
        self.__logout_link.click()
        return LoginPage(self.__driver)


class CartFeature:
    def __init__(self, driver):
        self.__driver = driver
        self.__cart = self.__driver.find_element(By.ID, 'shopping_cart_container')

    def get_cart(self):
        self.__cart.click()
        return CartPage(self.__driver)