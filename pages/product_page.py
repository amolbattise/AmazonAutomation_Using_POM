from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.qty_dropdown = (By.XPATH, "//span[text()='Quantity:']")
        self.add_to_cart_btn = (By.XPATH, "//span[text()='Add to Cart']")

    def get_price(self):

        try:
            price_elem = self.wait.until(
                EC.presence_of_element_located(
                    (By.ID, "//span[normalize-space()='249']")
                )
            )
        except:

            try:
                price_elem = self.driver.find_element(By.XPATH, "//span[normalize-space()='329']")
            except:

                price_elem = self.driver.find_element(By.ID, "priceblock_saleprice")

        return price_elem.text.strip().replace("₹", "").replace(",", "")

    def select_random_quantity(self, qty):
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element(*self.qty_dropdown))
        select.select_by_value(str(qty))

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()
