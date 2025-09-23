import pytest
import time
from selenium import webdriver, EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

from pages.search_results import SearchResults

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    time.sleep(3)
    yield driver
    driver.quit()

def test_amazon_product(driver, add_to_cart=None):
    # driver.get("https://www.amazon.in/")
    # time.sleep(3)


    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Amazon Basics Laptop Bag" + Keys.ENTER)

    results = SearchResults(driver)


    assert results.verify_results_header(), "Search results header not found"
    time.sleep(3)


    results.select_brand_checkbox("Amazon Basics")
    time.sleep(3)


    product_name = "Amazon Basics Laptop Bag Sleeve Case Cover Pouch"
    product_elem = results.find_product(product_name)
    time.sleep(3)



    assert product_elem is not None, "Product not found"


    product_elem.click()
    time.sleep(3)

    product_price = driver.find_element(By.XPATH, "//span[@class='a-price-whole']")
    product_price.click()
    time.sleep(3)

    wait1 = WebDriverWait(driver, 10)
    add_to_cart_btn = wait1.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
    add_to_cart_btn.click()








