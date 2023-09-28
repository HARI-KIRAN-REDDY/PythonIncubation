import os
import configparser


class ConfigUtil:
    @staticmethod
    def __get_config():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(script_dir, '../config.ini')
        config = configparser.ConfigParser()
        config.read(config_file_path)
        return config

    @staticmethod
    def get_browsers():
        config = ConfigUtil.__get_config()
        return config.get('BrowserSettings', 'BROWSERS').split(', ')

    @staticmethod
    def get_user_name():
        config = ConfigUtil.__get_config()
        return config.get('UserCredentials', 'USER_NAME')

    @staticmethod
    def get_password():
        config = ConfigUtil.__get_config()
        return config.get('UserCredentials', 'PASSWORD')

    @staticmethod
    def get_login_page_url():
        config = ConfigUtil.__get_config()
        return config.get('PageConstants', 'LOGIN_PAGE_URL')

    @staticmethod
    def get_dashboard_page_url():
        config = ConfigUtil.__get_config()
        return config.get('PageConstants', 'DASHBOARD_PAGE_URL')

    @staticmethod
    def get_backpack_product_name():
        config = ConfigUtil.__get_config()
        return config.get('PageConstants', 'BACKPACK_PRODUCT')

    @staticmethod
    def get_bike_light_product_name():
        config = ConfigUtil.__get_config()
        return config.get('PageConstants', 'BIKE_LIGHT_PRODUCT')
