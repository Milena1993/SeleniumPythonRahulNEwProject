from selenium.webdriver.common.by import By
from utilities.locators import Locators
from pages.checkout_page import CheckOutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ConfirmPage(Locators):
    
    def __init__(self, driver):
        super().__init__()
        self.driver = driver 

    def select_delivery_country(self):
        input_field= self.driver.find_element(By.ID, self.country_name)
        input_field.send_keys(self.country_option)
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located(((By.CSS_SELECTOR, self.suggested_overlay))))
        country = self.driver.find_element(By.CSS_SELECTOR, self.suggested_overlay)
        if country == self.suggested_country:
            country.click()
        return input_field.get_attribute("value")
        
                
    def confirmpage_element_click(self, locator_click):
        return CheckOutPage.checkoutpage_element_click(self, locator_click)

    def succes_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.success_message).text

    def confirmpage_element_dispaled(self, locator):
        return CheckOutPage.checkoutpage_element_displayed(self, locator)
        
