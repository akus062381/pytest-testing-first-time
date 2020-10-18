"""
These tests cover DuckDuckGo searches.
"""

from pages.homepage import AutomationTestingHomepage
from pages.result_page import AutomationTestingResultPage
from pages.shopping_cart import AutomationTestingShoppingCart
from pages.pop_up import AutomationTestingCartPopUp



def test_automation_testing_add_to_cart_feature(browser):
    homepage_page = AutomationTestingHomepage(browser)
    pop_up_page = AutomationTestingCartPopUp(browser)
    result_page = AutomationTestingResultPage(browser)
    cart_page = AutomationTestingShoppingCart(browser)
    LINK = "http://automationpractice.com/index.php?id_product=1&controller=product"

    # Given the automation testing website is displayed
    homepage_page.load()

    # When the user clicks on the add to cart button for the faded short sleeve t-shirts
    homepage_page.findElement(By.linkText("Faded Short Sleeve T-shirts")).click()

    # Then the item summary page is displayed


    # And the user clicks the Add to Cart button


    # Then the cart summary pop up displays


    # And the user clicks the Proceed to checkout button


    # And the cart is displayed showing that faded short sleeve tshirt has been added


    raise Exception("Incomplete Test")






 
