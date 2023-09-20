from selenium import webdriver
from selenium.webdriver.common.by import By
from exceptions.page_exceptions import IncompleteDetailsException
from .cart_feature import CartFeature
from .menu_feature import MenuFeature

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
