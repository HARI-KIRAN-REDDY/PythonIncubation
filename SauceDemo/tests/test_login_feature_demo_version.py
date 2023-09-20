from pages.login_page import *
from selenium import webdriver

def test_one():
    driver = webdriver.Chrome()
    login_page =  LoginPage(driver)
    login_page.enter_user_name('Standard_user')