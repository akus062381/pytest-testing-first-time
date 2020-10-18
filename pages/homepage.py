"""
This module contains instructions for loading the homepage and adding an item to the cart.
"""

from selenium.webdriver.common.by import By 
from selenium import webdriver


class AutomationTestingHomepage:

    URL = 'http://automationpractice.com/index.php'

    #BUTTON = driver.find_element_by_partial_link_text('Faded')
    BUTTON = '//a[@class="product-name"][@title="Faded Short Sleeve T-shirts"]'

    def __init__(self, browser):
        self.browser = browser
    
    def load(self):
        self.browser.get(self.URL)
    
    def click_item(self):
        button_element = self.browser.find_element(By.XPATH, self.BUTTON)
        print(button_element.text)
        button_element.click()
