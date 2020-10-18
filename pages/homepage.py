"""
This module contains instructions for loading the homepage and adding an item to the cart.
"""

from selenium.webdriver.common.by import By 
from selenium import webdriver

class AutomationTestingHomepage:

    URL = 'http://automationpractice.com/index.php'

    BUTTON_TO_CLICK = driver.find_element(By.LINK_TEXT, "Faded Short Sleeve T-shirts")



    def __init__(self, browser):
        self.browser = browser
    
    def load(self):
        self.browser.get(self.URL)
    
    def click_item(self, link):
        button_to_click = self.browser.find_element_by_link_text(*self.BUTTON_TO_CLICK)
