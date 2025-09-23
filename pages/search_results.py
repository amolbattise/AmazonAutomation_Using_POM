from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchResults:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def verify_results_header(self):
        try:
            header = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'results for')]"))
            )
            return True if header else False
        except:
            return False

    def select_brand_checkbox(self, brand_name="Amazon Basics"):
        try:
            brand_checkbox = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@aria-label,'Apply the filter amazon basics to narrow results')]//i[contains(@class,'a-icon a-icon-checkbox')]"))
            )
            self.driver.execute_script("arguments[0].click();", brand_checkbox)
            time.sleep(2)
        except:
            print(f"{brand_name} brand checkbox not found")

    def find_product(self, search_key):
        while True:
            self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class,'a-text-normal')]"))
            )
            products = self.driver.find_elements(By.XPATH, "//span[contains(text(),'Amazon Basics Laptop Bag Sleeve Case Cover Pouch for 15-Inch, 15.6-Inch Laptop for Men & Women | Slim Profile Neoprene, Soft Puffy Fabric Lining, 360° Protection, Smooth & Premium Zipper (Grey)')]")

            for prod in products:
                if search_key.lower() in prod.text.lower():

                    try:
                        link_elem = prod.find_element(By.XPATH, ".//ancestor::a")
                        return link_elem
                    except:
                        return prod  # fallback

            try:
                next_btn = self.driver.find_element(By.XPATH, "//a[contains(@class,'s-pagination-next')]")
                self.driver.execute_script("arguments[0].click();", next_btn)
                time.sleep(2)
            except:
                return None







    # def find_product_new(self):
    #     while True:
    #         self.wait.until(
    #             EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class,'a-text-normal')]"))
    #         )
    #         products1 = self.driver.find_elements(By.XPATH, "//span[contains(text(),'Amazon Basics Laptop Bag Sleeve Case Cover Pouch for 15-Inch, 15.6-Inch Laptop for Men & Women | Slim Profile Neoprene, Soft Puffy Fabric Lining, 360° Protection, Smooth & Premium Zipper (Grey)')]")
    #         for products1.is_displayed() == False:
    #             if  products1.is_displayed() == False:
    #                 next_btn = self.driver.find_element(By.XPATH, "//a[contains(@class,'s-pagination-next')]")
    #                 self.driver.execute_script("arguments[0].click();", next_btn)
    #                 time.sleep(2)
    #             else:
    #                 print("product found")
    #                 break


