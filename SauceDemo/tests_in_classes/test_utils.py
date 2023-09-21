from  selenium import webdriver
from config import BROWSER

def get_browser():
    driver = None
    if BROWSER == 'chrome':
        driver = webdriver.Chrome()
    elif BROWSER == 'edge':
        driver = webdriver.Edge()
    elif BROWSER == 'firefox':
        driver = webdriver.Firefox()
    return driver