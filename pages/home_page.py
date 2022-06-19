from selenium.webdriver.common.by import By
from utilities.locators import Locators

class HomePage(Locators):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver 
    
    shop = (By.LINK_TEXT, Locators.shop_link)

    def shop_items(self):
        return self.driver.find_element(*HomePage.shop)
