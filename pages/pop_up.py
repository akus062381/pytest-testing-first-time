"""
This module shows the steps when the cart pop appears and enables the user to verify the item is in the cart.
"""

from selenium.webdriver.common.by import By 

class AutomationTestingCartPopUp:

    CART_LINK = (By.LINK_TEXT, 'http://automationpractice.com/index.php?controller=order')

    def __init__(self, browser):
        self.browser = browser

    def title(self):
        return ""

    def proceed_to_checkout(self):
        pass