from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from abc import ABC, abstractmethod
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from my_constants.pages_constants import DASHBOARD_PAGE_URL, BACKPACK_PRODUCT, BIKE_LIGHT_PRODUCT
from exceptions.page_exceptions import InvalidCredentialsException, IncompleteDetailsException, ZeroProductsInCartException, NoSuchProductInCartException
from time import sleep

class Cart(ABC):
    @abstractmethod
    def get_cart(self):
        pass
class Menu(ABC):
    @abstractmethod
    def get_menu(self):
        pass

class LoginPage:
    def __init__(self, driver: webdriver):
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
        if self.__driver.current_url == DASHBOARD_PAGE_URL:
            return DashboardPage(self.__driver)
        else:
            error_message = self.__error_element.text
            raise InvalidCredentialsException(error_message)


class DashboardPage(Cart, Menu):
    def __init__(self, driver):
        self.__cart_feature = CartFeature.get_cart(driver)
        self.__menu_feature = MenuFeature(driver)
        self.__driver = driver
        self.__product_sorting_select_container = Select(
            self.__driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select'))
        self.__backpack_product_button = self.__driver.find_element(By.CSS_SELECTOR, '[id*="backpack"]')
        self.__bike_light_product_button = self.__driver.find_element(By.CSS_SELECTOR, '[id*="bike-light"]')
        self.__list_of_available_products_on_dashboard = self.__driver.find_elements(By.XPATH, '//div[@class = "inventory_item"]//a/div')

    def sort_products_by_price(self):
        self.__product_sorting_select_container.select_by_index(2)
        return DashboardPage(self.__driver)

    def sort_products_by_name_a_to_z(self):
        self.__product_sorting_select_container.select_by_index(0)
        return DashboardPage(self.__driver)
    def sort_products_by_name_z_to_a(self):
        self.__product_sorting_select_container.select_by_index(1)
        return DashboardPage(self.__driver)

    def get_list_of_available_products_on_dashboard(self):
        return [product.text for product in self.__list_of_available_products_on_dashboard]

    def add_backpack_to_cart(self):
        if self.__backpack_product_button.text == 'Add to cart':
            self.__cart_feature.add_product_to_cart(BACKPACK_PRODUCT)
            self.__backpack_product_button.click()
        return DashboardPage(self.__driver)

    def remove_backpack_from_cart(self):
        if self.__backpack_product_button.text == 'Remove':
            self.__backpack_product_button.click()
            self.__cart_feature.remove_product_from_cart(BACKPACK_PRODUCT)
        return DashboardPage(self.__driver)

    def add_bike_light_to_cart(self):
        if self.__bike_light_product_button.text == 'Add to cart':
            self.__cart_feature.add_product_to_cart(BIKE_LIGHT_PRODUCT)
            self.__bike_light_product_button.click()
        return DashboardPage(self.__driver)

    def remove_bike_light_from_cart(self):
        if self.__bike_light_product_button.text == 'Remove':
            self.__bike_light_product_button.click()
            self.__cart_feature.remove_product_from_cart(BIKE_LIGHT_PRODUCT)
        return DashboardPage(self.__driver)

    def get_menu(self):
        return self.__menu_feature.get_menu_feature()

    def get_cart(self):
        return self.__cart_feature.get_cart(self.__driver)


class CheckoutPageOne(Cart, Menu):
    def __init__(self, driver: webdriver):
        self.__cart_feature = CartFeature.get_cart(driver)
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

    def continue_to_final_step_in_checkout(self):
        list_of_text_fields = [self.__first_name_text_box, self.__last_name_text_box, self.__zipcode_text_box]
        if not self.__is_no_field_empty(list_of_text_fields):
            raise IncompleteDetailsException('Makesure you entered first-name, last-name and zipcode fields')
        self.__continue_button.click()
        return CheckoutPageTwo(self.__driver)

    def __is_no_field_empty(self, text_boxes):
        for text_box in text_boxes:
            if text_box.get_attribute('value') == '':
                return False
        return True

    def get_menu(self):
        return self.__menu_feature.get_menu_feature()

    def get_cart(self):
        return self.__cart_feature.get_cart(self.__driver)


class CheckoutPageTwo(Cart, Menu):
    def __init__(self, driver):
        self.__cart_feature = CartFeature.get_cart(driver)
        self.__menu_feature = MenuFeature(driver)
        self.__driver = driver
        sleep(2)
        self.__finish_btn = self.__driver.find_element(By.ID, 'finish')

    def confirm_order(self):
        self.__finish_btn.click()
        return CheckoutCompletePage(self.__driver)

    def get_menu(self):
        return self.__menu_feature.get_menu_feature()

    def get_cart(self):
        return self.__cart_feature.get_cart(self.__driver)


class CheckoutCompletePage:
    def __init__(self, driver: webdriver):
        self.__driver = driver
        self.__back_to_home_btn = self.__driver.find_element(By.ID, 'back-to-products')

    def back_to_dashboard(self):
        self.__back_to_home_btn.click()
        return DashboardPage(self.__driver)


class CartPage(Cart, Menu):
    def __init__(self, driver):
        self.__cart_feature = CartFeature.get_cart(driver)
        self.__menu_feature = MenuFeature(driver)
        self.__driver = driver
        self.__continue_to_shopping_btn = self.__driver.find_element(By.ID, 'continue-shopping')
        self.__continue_to_checkout_btn = self.__driver.find_element(By.ID, 'checkout')
        try:
            self.__list_of_products = self.__driver.find_elements(By.XPATH, '//div[@class="cart_list"]//a/div[@class="inventory_item_name"]')
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


class MenuFeature:
    def __init__(self, driver = webdriver.Chrome):
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
        return LoginPage(self.__driver)


class CartFeature:
    __instance = None

    def __new__(cls, driver):
        if cls.__instance is None:
            cls.__instance = super(CartFeature, cls).__new__(cls)
            cls.__instance.__driver = driver
            cls.__instance.__cart = cls.__instance.__driver.find_element(By.ID, 'shopping_cart_container')
            cls.__instance.__list_of_products = []
            cls.__instance.__no_of_items_in_cart_element = cls.__instance.__driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
        return cls.__instance

    @staticmethod
    def get_cart(driver):
        return CartFeature(driver)

    def get_cart_page(self):
        self.__cart.click()
        return CartPage(self.__driver)

    def add_product_to_cart(self, product):
        if product not in self.__list_of_products:
            self.__list_of_products.append(product)

    def remove_product_from_cart(self, product):
        # Need to change this mechanism, this is for demo purpose
        if product in self.__list_of_products:
            self.__list_of_products.remove(product)
        else:
            raise NoSuchProductInCartException

    def get_no_of_products_in_cart(self):
        try:
            return int(self.__no_of_items_in_cart_element.text)
        except StaleElementReferenceException:
            return 0