from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class totalPrice():
    def __init__(self, driver):
        self.wait = self.wait
        self.driver = driver
        wait = WebDriverWait(driver, 10)

        self.total_price = (By.CSS_SELECTOR, ".summary_total_label")
        self.finish_btn =  (By.ID,"finish")
        self.checkout_complete = (By.ID, "checkout_complete_container")
        self.back_btn = (By.CSS_SELECTOR,"#back-to-products")

    def sum_of_total_price(self):
        self.wait.until(EC.visibility_of_element_located(self.total_price))
        print("Checkout summary displayed successfully")


    def click_finish(self):
        self.driver.find_element(*self.finish_btn).click()

    def checkout_complete(self):
        self.wait.until(EC.visibility_of_element_located(self.checkout_complete))
        print("Thank you for your order!")

    def return_to_homepage(self):
        self.driver.find_element( self.back_btn).click()





