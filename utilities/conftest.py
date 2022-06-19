from lib2to3.pgen2 import driver
import pytest 
from selenium import webdriver
import json


@pytest.fixture(autouse = True)
def config(request):
    with open('utilities/config.json') as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(autouse = True)
def setup(config, request):
    driver = webdriver.Chrome(config["chrome_path"])
    driver.implicitly_wait(10)
    driver.get(config["url"])
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()