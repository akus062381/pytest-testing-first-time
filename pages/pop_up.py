"""
This module shows the steps when the cart pop appears and enables the user to verify the item is in the cart.
"""

from selenium.webdriver.common.by import By 

class AutomationTestingCartPopUp:

    ADD_TO_CART = '//div/p[@id="add_to_cart"]/button[@name="Submit"]'
    PROCEED_TO_CHECKOUT = '//a[@title="Proceed to checkout"]'

    def __init__(self, browser):
        self.browser = browser


    def add_to_cart(self):
        add_to_cart_element = self.browser.find_element(By.XPATH, self.ADD_TO_CART)
        add_to_cart_element.click()

    def proceed_to_checkout(self):
        proceed_to_checkout_element = self.browser.find_element(By.XPATH, self.PROCEED_TO_CHECKOUT)
        proceed_to_checkout_element.click()
        