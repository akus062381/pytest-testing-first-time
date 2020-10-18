"""
This module contains instructions for testing whether the item was added to the shopping cart correctly.
"""

from selenium.webdriver.common.by import By 

class AutomationTestingShoppingCart:

    VERIFY_ITEM = (By.LINK_TEXT, 'http://automationpractice.com/index.php?id_product=1&controller=product#/size-s/color-orange')

    def __init__(self, browser):
        self.browser = browser
    
    def selected_item_in_cart(self):
        return []
    
   
    
