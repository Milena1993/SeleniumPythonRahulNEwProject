from pickle import TRUE
import re
import pytest 
from actions import Actions
from locators import Locators
import time


@pytest.mark.usefixtures('driver')

class Test():

    
    #Assert page is opened (url, title)
    def test_title(self,driver):
        action = Actions(driver)
        actual_result = action.get_page(self)
        expected_result = ("GreenKart - veg and fruits kart", "https://rahulshettyacademy.com/seleniumPractise/#/")
        assert actual_result == expected_result
        print(actual_result)


    def test_order_flow(self, driver):
        action = Actions(driver)
        action.add_mango_to_card()
    
    #Assert Items and Price are shown as expected in the cart info (top right)
        actual_result = action.selected_item_price_check()
        expected_result = action.item_price_check()
        assert actual_result == expected_result

        actual_result = action.selected_item_quantity_check()
        expected_result = action.item_quantity_check()
        assert actual_result == expected_result

    # Click on the cart icon
        action.cart_icon_click()
        assert action.cart_popup_check() == True
        assert action.displayed_item_name_check() == 'Mango - 1 Kg'
        assert action.displayed_item_price_check() == action.item_price_check()
        
    # Click on "Proceed to checkout" button
        action.proceed_to_checkout_click()
        
    #Assert cart page is opened 
        assert action.product_table_check() == True

    #Assert only one item is shown in the cart
        assert action.table_data_check() == True
        assert action.total_amount_check() == True
        assert action.table_row_quantity_check()==1
    
    #Click on "Place Order"
        action.place_order_click()

    #Select country
        action.select_delivery_country()
        assert action.select_delivery_country() == "Armenia"

    #Check "Terms & Conditions" checkbox
        action.checkbox_selection()
        assert action.checkbox_status() == True

    #Click on "Proceed" button
        action.proceed_click()

    # Assert Success message is shown  
        action.final_success_message()
        assert action.final_success_message() == True
        time.sleep(4)