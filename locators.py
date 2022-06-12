class Locators:
    product_list = '//div[@class="product"]' #By Xpath 
    requested_product = "Mango - 1 Kg"
    product_name = 'h4' #By Xpath 
    add_to_card_button = 'div/button' #By Xpath
    item_quantity = '//input[@class="quantity"]' #By xpath
    item_price = "div > div:nth-child(18) > p" #By CSS selector
    selected_top_product_price = '//tbody/tr[2]/td[3]/strong[1]' #By xpath
    selected_product_quantity = '//tbody/tr[1]/td[3]/strong[1]' #By xpath
    cart_icon =  'img[alt ="Cart"]' #By CSS selector
    cart_popup = '.cart> .cart-preview'#By CSS selector
    selected_product_name = '.cart-preview .product-info > .product-name'#By CSS selector
    selected_product_price = '.cart-preview .product-info > .product-price' #by CSS selector
    proceed_to_checkout_button = '//button[text()="PROCEED TO CHECKOUT"]' #By Xpath
    product_table = '.products-wrapper' #By CSS selector
    table_price ="td:nth-child(4) .amount" #By CSS selector
    table_item_quantity = "td > .quantity" #By CSS selector
    table_total_price = "td:nth-child(5) .amount"  #By CSS selector
    table_total_amount = 'span.totAmt' #By CSS selecto
    table_row= "div .products tbody tr" #By CSS selector
    place_order_button = '//button[text()= "Place Order"]' #By xpath 
    checkbox = 'chkAgree' #byclassname
    select_country = 'select' #by tagname
    country_option = "Armenia"
    proceed_button = '//button[text()= "Proceed"]' #By xpath 
    success_text = "//*[contains(text(), 'Thank you, your order has been placed successfully')]"
    

   
 