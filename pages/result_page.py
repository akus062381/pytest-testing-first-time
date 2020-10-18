"""
This module contains Automation Testing pop-up that appears after adding an item to the cart.
"""

from selenium.webdriver.common.by import By 

class AutomationTestingResultPage:

    ADD_TO_CART = (By.NAME, 'Submit')
    PICTURE_VERIFY = (By.ID, 'bigpic')

    def __init__(self, browser):
        self.browser = browser
    
    def verify_item_selected(self):
        pass
    
    def add_item_to_cart(self):
        pass
    
   

