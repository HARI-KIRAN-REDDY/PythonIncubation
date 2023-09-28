from selenium.webdriver.common.by import By
from exceptions.page_exceptions import NoSuchProductInCartException


class CartFeature:
    __instance = None

    def __new__(cls, driver):
        if cls.__instance is None:
            cls.__instance = super(CartFeature, cls).__new__(cls)
            cls.__instance.__list_of_products = []
        cls.__instance.__driver = driver
        cls.__instance.__cart = cls.__instance.__driver.find_element(By.ID, 'shopping_cart_container')
        cls.__instance.__no_of_items_in_cart_element = cls.__instance.__driver.find_element(By.XPATH,
                                                                                            '//a[@class="shopping_cart_link"]')
        return cls.__instance

    @staticmethod
    def get_cart(driver):
        return CartFeature(driver)

    def get_cart_page(self):
        self.__cart.click()
        from pages.cart_page import CartPage
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
        except ValueError:
            return 0
