from numpy import broadcast
import pytest 
from selenium import webdriver

@pytest.fixture(autouse = True)
def driver():
    browser = webdriver.Chrome(executable_path = "chromedriver/chromedriver.exe")
    browser.implicitly_wait(10)
    browser.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    browser.maximize_window()
    yield browser
    browser.quit()

