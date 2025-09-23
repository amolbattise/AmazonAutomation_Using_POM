from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_qty = (By.NAME, "quantity")
        self.cart_count = (By.ID, "nav-cart-count")

    def get_quantity(self):
        return self.driver.find_element(*self.cart_qty).get_attribute("value")

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_count).text
