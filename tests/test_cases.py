from pickle import TRUE
import re
import pytest
from pages.checkout_page import CheckOutPage 
from pages.home_page import HomePage
from pages.confirm_page import ConfirmPage
from utilities.locators import Locators
from utilities.conftest import setup, config
import time



@pytest.mark.usefixtures('setup', 'config')
class Test(Locators):
    def test_order_flow(self):

        #go to Shop page
        homePage = HomePage(self.driver)
        homePage.shop_items().click()

        #select product
        checkoutPage = CheckOutPage(self.driver)
        checkoutPage.choose_product()
      
        #click on checkout button
        checkoutPage.checkoutpage_element_click(self.checkout_button)

        #assert that item is choosed correctly
        assert checkoutPage.checkoutpage_element_text(self.choosed_product) == checkoutPage.checkoutpage_element_text(self.selected_item_name)

        #assert that item is in stock
        assert checkoutPage.checkoutpage_element_displayed(self.in_stock) == True

        #assert the correctness of item price and cost 
        assert checkoutPage.price_cost_check() == True

        #click on checkout button
        checkoutPage.checkoutpage_element_click(self.checkout_inside_button)
        
        # choose delivery country 
        confirmPage = ConfirmPage(self.driver)
        confirmPage.select_delivery_country()
        print(confirmPage.select_delivery_country())

        #click on term and confition field 
        confirmPage.confirmpage_element_click(self.terms_and_confitions_field)

        #clcik on purcase button
        confirmPage.confirmpage_element_click(self.submit_button)

        #assert that sucess message is apperaed
        assert self.success_text in  confirmPage.succes_message()

        
    def test_product_remove(self):
        homePage = HomePage(self.driver)
        homePage.shop_items().click()
        checkoutPage = CheckOutPage(self.driver)
        checkoutPage.choose_product()
        checkoutPage.checkoutpage_element_click(self.checkout_button)

        #click on remove button
        checkoutPage.checkoutpage_element_click(self.remove_button)

        #assert that selected product is removed 
        confirmPage = ConfirmPage(self.driver)
        assert confirmPage.confirmpage_element_dispaled(self.no_item) == True
     