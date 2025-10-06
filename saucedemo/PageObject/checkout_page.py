from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Checkout():
    def __init__(self, driver):
        self.wait = self.wait
        self.driver = driver
        wait = WebDriverWait(driver, 10)

        self.checkout_container = (By.ID,"checkout_info_container")
        self.firstname = (By.ID,"first-name")
        self.lastname = (By.ID,"last-name")
        self.postalcode = (By.ID,"postal-code")
        self.continue_btn = (By.ID,"continue")


    def checkout_information(self):
        self.wait.until(EC.visibility_of_element_located(self.checkout_container))

    def fill_personal_details(self, firstname, lastname, postalcode):
        self.driver.find_element(*self.firstname).send_keys(firstname)
        self.driver.find_element(*self.lastname).send_keys(lastname)
        self.driver.find_element(*self.postalcode).send_keys(postalcode)

    def click_continue(self):
        self.driver.find_element(self.continue_btn).click()




