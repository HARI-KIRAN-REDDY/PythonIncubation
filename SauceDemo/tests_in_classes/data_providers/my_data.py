# from tests_in_classes.test_utils import get_valid_login_credentials, get_invalid_login_credentials
import csv
import os

abs_path = os.path.dirname(os.path.abspath(__file__))

def fetch_username_password_data(file_name):
    data = []
    my_file = open(os.path.join(abs_path, file_name), mode='r')
    reader = csv.DictReader(my_file)
    for row in reader:
        data.append({'user_name':row['user_name'], 'password':row['password']})
    my_file.close()
    return data
def get_invalid_login_credentials():
    file_name = 'invalid_username_passwords.csv'
    return fetch_username_password_data(file_name)
def get_valid_login_credentials():
    file_name = 'valid_username_passwords.csv'
    return fetch_username_password_data(file_name)

