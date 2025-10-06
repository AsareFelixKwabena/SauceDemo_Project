import time
from faker import Faker
from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

#service_obj = Service("C:\\Users\\QWABENA EL\\Downloads\\chromedriver-win64\\chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)
faker = Faker()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 10)

first_name = faker.first_name()
last_name = faker.last_name()
postal_code = faker.postalcode()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product_sort_container")))
dropdown = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")
Select(dropdown).select_by_value("lohi")
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
items = driver.find_elements(By.CLASS_NAME, "inventory_item")

for i in range(3):
    name = items[i].find_element(By.CLASS_NAME, "inventory_item_name").text
    print(f"Item {i + 1}: {name}")

    add_button = items[i].find_element(By.TAG_NAME, "button")
    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    add_button.click()
    time.sleep(1)

driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".cart_list")))
driver.find_element(By.ID,"checkout").click()

wait.until(EC.visibility_of_element_located((By.ID,"checkout_info_container")))
driver.find_element(By.ID,"first-name").send_keys(first_name)
driver.find_element(By.ID,"last-name").send_keys(last_name)
driver.find_element(By.ID,"postal-code").send_keys(postal_code)
driver.find_element(By.ID,"continue").click()

#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".cart_list")))
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
print("Checkout summary displayed successfully")
driver.find_element(By.ID,"finish").click()
wait.until(EC.visibility_of_element_located((By.ID, "checkout_complete_container")))
print("Thank you for your order!")
driver.find_element(By.CSS_SELECTOR,"#back-to-products").click()
time.sleep(3)
driver.quit()
