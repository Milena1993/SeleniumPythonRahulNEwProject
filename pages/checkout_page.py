from selenium.webdriver.common.by import By
from utilities.locators import Locators
from selenium.webdriver.support.ui import Select

class CheckOutPage(Locators):
    
    def __init__(self, driver):
        super().__init__()
        self.driver = driver 

    def choose_product(self):
        products = self.driver.find_elements(By.XPATH, self.products)
        for product in products:
            productName = product.find_element(By.XPATH, self.product_name).text
            if productName == self.choosed_product:
                product.find_element(By.XPATH, self.add_button).click()
      
    def checkoutpage_element_click(self, locator_click):
        item_click = self.driver.find_element(By.XPATH, locator_click)
        item_click.click()

    def checkoutpage_element_text(self, locator_text):
        item_text = self.driver.find_element(By.LINK_TEXT, locator_text)
        return item_text.text

    def checkoutpage_element_displayed(self, locator):
        item_display = self.driver.find_element(By.CSS_SELECTOR, locator)
        return item_display.is_displayed()

    def price_cost_check(self):
        item_price = self.driver.find_element(By.CSS_SELECTOR,self.item_price).text
        item_cost = self.driver.find_element(By.CSS_SELECTOR,self.item_cost).text
        return  item_price == item_cost