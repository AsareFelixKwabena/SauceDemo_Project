from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ShoppingCart():
    def __init__(self, driver):
        self.wait = self.wait
        self.driver = driver
        wait = WebDriverWait(driver, 10)

        self.cart_link = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.cart_list = (By.CSS_SELECTOR,".cart_list")
        self.checkout = (By.ID,"checkout")


    def shopping_cart(self):
        self.driver.find_element(*self.cart_link)

    def cart_list(self):
        self.wait.until(EC.visibility_of_element_located(self.cart_list))

    def click_checkout(self):
        self.driver.find_element(self.checkout).click()


