"""
These tests cover AutomationTesting checks.
"""
from selenium import webdriver
from pages.homepage import AutomationTestingHomepage
from pages.shopping_cart import AutomationTestingShoppingCart
from pages.pop_up import AutomationTestingCartPopUp



def test_automation_testing_add_to_cart_feature(browser):
    homepage_page = AutomationTestingHomepage(browser)
    pop_up_page = AutomationTestingCartPopUp(browser)
    cart_page = AutomationTestingShoppingCart(browser)
    #BUTTON = driver.find_element_by_link_text('Faded Short Sleeve T-shirts')
    

    # Given the automation testing website is displayed
    homepage_page.load()

    # When the user clicks on the item faded short sleeve t-shirts
    homepage_page.click_item()


    # And the user clicks the Add to Cart button
    pop_up_page.add_to_cart()


    # And the user clicks the Proceed to checkout button
    pop_up_page.proceed_to_checkout()




    






 
