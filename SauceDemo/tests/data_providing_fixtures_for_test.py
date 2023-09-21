import csv

import pytest


@pytest.fixture()
def get_invalid_login_credentials():
    file_name = 'data_providers/invalid_username_passwords.csv'
    return fetch_username_password_data(file_name)

@pytest.fixture(params=[(1,2), (2,3)])
def ok(request):
    return request.param
@pytest.fixture()
def get_valid_login_credentials():
    file_name = 'data_providers/valid_username_passwords.csv'
    return fetch_username_password_data(file_name)


def fetch_username_password_data(file_name):
    data = []
    my_file = open(file_name, mode='r')
    reader = csv.DictReader(my_file)
    for row in reader:
        data.append((row['user_name'], row['password']))
    my_file.close()
    return data

def test_me(ok):
    print(ok)