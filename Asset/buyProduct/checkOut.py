from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Asset.buyProduct.sourceCO import resource
from selenium.webdriver.support.ui import Select
import time

locator = resource()

def checkout(driver):
    first_name = driver.find_element(By.XPATH, locator.first_name)
    first_name.send_keys(Keys.CONTROL + "a") 
    first_name.send_keys(Keys.BACKSPACE)
    first_name.send_keys("Jim")
    time.sleep(2)
    first_name = driver.find_element(By.XPATH, locator.last_name)
    first_name.send_keys(Keys.CONTROL + "a") 
    first_name.send_keys(Keys.BACKSPACE)
    first_name.send_keys("Carry")
    time.sleep(2)
    company = driver.find_element(By.XPATH, locator.company)
    company.send_keys("Sony")
    time.sleep(2)
    street_adress = driver.find_element(By.XPATH, locator.street_adress)
    street_adress.send_keys("Broklyn St 12 Avenue")
    time.sleep(2)
    city = driver.find_element(By.XPATH, locator.city)
    city.send_keys("New York")
    time.sleep(2)
    dropdown_element_region = driver.find_element(By.XPATH, locator.select_region)
    select_region = Select(dropdown_element_region)
    select_region.select_by_visible_text("Alaska")
    time.sleep(2)
    post_code = driver.find_element(By.XPATH, locator.post_code)
    post_code.send_keys("12123")
    time.sleep(2)
    dropdown_element_country = driver.find_element(By.XPATH, locator.select_country)
    select_country = Select(dropdown_element_country)
    select_country.select_by_visible_text("United States")
    time.sleep(2)
    phone_number = driver.find_element(By.XPATH, locator.phone_number)
    phone_number.send_keys("082145550364")
    time.sleep(2)
    driver.find_element(By.XPATH, locator.payment).click()
    time.sleep(2)
    driver.find_element(By.XPATH, locator.next).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, locator.wait_element_reviewandpayment))
    )
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, locator.wait_element_check))
    )
    driver.find_element(By.XPATH, locator.place_order).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, locator.recipt))
    )
    driver.find_element(By.XPATH, locator.continue_shopping).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, locator.home_menu))
    )
    time.sleep(5)