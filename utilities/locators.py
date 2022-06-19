class Locators:
    shop_link = 'Shop' #By link_text
    item_name = '.card-title a' #By CSS selector
    choosed_product = "Blackberry" #By link text 
    products = "//div[@class='card h-100']" #By Xpath
    product_name = "div/h4/a" #By Xpath
    add_button = "div/button" #By Xpath
    checkout_button = '//a[@class="nav-link btn btn-primary"]' #By CSS selector
    selected_item_name = "Blackberry" #By link text 
    in_stock = ".text-success >strong" #By CSS selector
    item_quantity = 'exampleInputEmail1' #By ID
    item_price = '.text-center:nth-child(3) > strong:nth-child(1)' #By CSS selector
    item_cost = '.text-center:nth-child(4) > strong:nth-child(1)' #By CSS selector
    checkout_inside_button = "//button[@class='btn btn-success']" #By Xpath
    remove_button = "//button[@class ='btn btn-danger']"  #By Xpath
    no_item = 'h3 >strong'  #By CSS selector
    country_name = "country" #by ID
    country_option ="arm"
    # suggested_overlay = "Armenia" #By link text 
    suggested_overlay = '.suggestions >ul > li >a'   #By CSS selector
    suggested_country ="Armenia" 
    terms_and_confitions_field = "//div[@class='checkbox checkbox-primary']" #By Xpath
    submit_button = "//input[@type='submit']" #By Xpath
    success_message = ".alert-success" #By CSS selector
    success_text = 'Thank you! Your order'
 