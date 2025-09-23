import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AmazonHome:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.XPATH, "//input[@id='twotabsearchtextbox']")


    def search(self, keyword):
        self.driver.find_element(*self.search_box).send_keys(keyword + Keys.ENTER)
