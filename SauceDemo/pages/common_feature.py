from abc import ABC, abstractmethod


class Cart(ABC):
    @abstractmethod
    def get_cart(self):
        pass


class Menu(ABC):
    @abstractmethod
    def get_menu(self):
        pass
