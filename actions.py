from locators import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Actions(Locators):


    def __init__(self, driver):
        super().__init__()
        self.driver = driver 

    def get_page(self, driver):
        driver = self.driver
        get_title = driver.title
        current_url = driver.current_url
        return get_title, current_url

    def add_mango_to_card(self):
        products =  self.driver.find_elements(By.XPATH, self.product_list)
        print(products)
        for product in products:
            productName = product.find_element(By.XPATH, self.product_name).text
            if productName == self.requested_product:
                add_mango = product.find_element(By.XPATH, self.add_to_card_button)
                add_mango.click()

    def item_price_check(self):
        item_price = self.driver.find_element(By.CSS_SELECTOR, self.item_price)
        return item_price.text

    def selected_item_price_check(self):
        item_price = self.driver.find_element(By.XPATH, self.selected_top_product_price)
        return item_price.text

    def item_quantity_check(self):
        quantity_check =self.driver.find_element(By.XPATH, self.item_quantity)
        return  quantity_check.get_property("value")

    def selected_item_quantity_check(self):
        quantity_check = self.driver.find_element(By.XPATH, self.selected_product_quantity)
        return quantity_check.text

    def cart_icon_click(self):
        cart_icon = self.driver.find_element(By.CSS_SELECTOR, self.cart_icon)
        cart_icon.click()

    def cart_popup_check(self):
        cart_popup = self.driver.find_element(By.CSS_SELECTOR,self.cart_popup)
        return cart_popup.is_displayed()

    def displayed_item_name_check(self):
        displayed_item = self.driver.find_element(By.CSS_SELECTOR, self.selected_product_name)
        return displayed_item.text

    def displayed_item_price_check(self):
        displayed_item = self.driver.find_element(By.CSS_SELECTOR, self.selected_product_price).text
        return displayed_item

    def proceed_to_checkout_click(self):
        proceed_to_checkout = self.driver.find_element(By.XPATH,self.proceed_to_checkout_button)
        proceed_to_checkout.click()
       
    def product_table_check(self):
        product_table = self.driver.find_element(By.CSS_SELECTOR,self.product_table)
        return product_table.is_displayed()
    
    def table_data_check(self):
        table_price = self.driver.find_element(By.CSS_SELECTOR,self.table_price).text
        table_item_quantity = self.driver.find_element(By.CSS_SELECTOR,self.table_item_quantity).text
        table_total_price = self.driver.find_element(By.CSS_SELECTOR,self.table_total_price).text
        return int(table_total_price) == int(table_price) * int(table_item_quantity)

    def total_amount_check(self):
        table_total_price = self.driver.find_element(By.CSS_SELECTOR,self.table_total_price).text
        total_amount = self.driver.find_element(By.CSS_SELECTOR,self.table_total_amount).text
        return int(table_total_price) == int(total_amount)


    def table_row_quantity_check(self):
        table_row = self.driver.find_elements(By.CSS_SELECTOR,self.table_row)
        return(len(table_row))

    def place_order_click(self):
        place_order = self.driver.find_element(By.XPATH, self.place_order_button)
        place_order.click()

    def select_delivery_country(self):
        select_country = self.driver.find_element(By.TAG_NAME, self.select_country)
        country = Select(select_country)
        country.select_by_visible_text(self.country_option)
        return country.first_selected_option.get_attribute("value")

    def checkbox_selection(self):
        select_checkbox = self.driver.find_element(By.CLASS_NAME, self.checkbox)
        select_checkbox.click()
    
    def checkbox_status(self):
        select_checkbox = self.driver.find_element(By.CLASS_NAME, self.checkbox)
        status = select_checkbox.is_selected()
        return status
    
    def proceed_click(self):
        proceed = self.driver.find_element(By.XPATH, self.proceed_button)
        proceed.click()
        

    def final_success_message(self):
        success_message = self.driver.find_element(By.XPATH, self.success_text)
        status = success_message.is_displayed()
        return status
        
   
       


    