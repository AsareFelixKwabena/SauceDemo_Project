import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



class HomePage():
    def __init__(self, driver):
        self.wait = self.wait
        self.driver = driver
        wait = WebDriverWait(driver, 10)

        self.sort_dropdown = (By.CSS_SELECTOR, ".product_sort_container")
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.add_button = (By.TAG_NAME, "button")

    def sort_products(self, value="lohi"):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.sort_dropdown))
        Select(dropdown).select_by_value(value)

        self.wait.until(EC.text_to_be_present_in_element(self.inventory_items))

    def get_items(self):
        return self.driver.find_elements(*self.inventory_items)

    def print_and_add_first_n_items(self, n=3):
        items = self.get_items()
        for i in range(3):
            name = items[i].find_element(*self.item_name).text
            print(f"Item {i + 1}: {name}")

        add_button = items[i].find_element(*self.add_button)
        self.wait.until(EC.element_to_be_clickable(self.add_button))
        add_button.click()
        time.sleep(1)
