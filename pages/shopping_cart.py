"""
This module contains instructions for testing whether the item was added to the shopping cart correctly.
"""

from selenium.webdriver.common.by import By 

class AutomationTestingShoppingCart:

    RESULT_LINK = '//p[@class="product-name"]/a'


    def __init__(self, browser):
        self.browser = browser
    
    def selected_item_in_cart(self):
        link = self.browser.find_element(By.XPATH, self.RESULT_LINK)
        return link
    
   
    
