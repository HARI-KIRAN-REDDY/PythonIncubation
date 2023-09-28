import csv
import os
import sys

class TestDataGetter:
    @staticmethod
    def __fetch_username_password_data(file_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        abs_path = os.path.abspath(os.path.join(script_dir, '..'))
        data = []
        my_file = open(os.path.join(abs_path, file_name), mode='r')
        reader = csv.DictReader(my_file)
        for row in reader:
            data.append({'user_name': row['user_name'], 'password': row['password']})
        my_file.close()
        return data

    @staticmethod
    def get_invalid_login_credentials():
        file_name = 'test_data/invalid_username_passwords.csv'
        return TestDataGetter.__fetch_username_password_data(file_name)

    @staticmethod
    def get_valid_login_credentials():
        file_name = 'test_data/valid_username_passwords.csv'
        return TestDataGetter.__fetch_username_password_data(file_name)

