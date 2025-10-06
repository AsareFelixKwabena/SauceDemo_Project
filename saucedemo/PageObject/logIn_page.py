from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from saucedemo.tests.e2e import name


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(driver, 10)

        self.enter_username= (By.ID, "user-name")
        self.enter_password = (By.ID, "password")
        self.click_login = (By.ID, "login-button")

    def enter_username(self, username):
        self.driver.find_element(*self.enter_username).send_keys(username)
        print("Username entered:")

    def enter_password(self, password):
        self.driver.find_element(*self.enter_password).send_keys(password)
        print("Password entered")


    def click_login(self):
        self.driver.find_element(*self.click_login).click()

