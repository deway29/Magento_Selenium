from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Asset.addtoChart.sourceAdditem import resource
import time

locator = resource()

def additem(driver):
    driver.find_element(By.XPATH, locator.product).click()
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, locator.product_menu))
    )
    driver.find_element(By.XPATH, locator.size).click()
    time.sleep(2)
    element_hover = driver.find_element(By.XPATH, locator.scroll)
    ActionChains(driver).move_to_element(element_hover).perform()
    time.sleep(2)
    driver.find_element(By.XPATH, locator.color).click()
    time.sleep(2)
    input_item = driver.find_element(By.XPATH, locator.quantity)
    input_item.send_keys(Keys.CONTROL + "a")  
    input_item.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    input_item.send_keys("4") 
    time.sleep(2)
    driver.find_element(By.XPATH, locator.checkout).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, locator.alert_succsess))
    )
    driver.find_element(By.XPATH, locator.cart_button).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, locator.item_cart))
    )
    driver.find_element(By.XPATH, locator.checkout_btn).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, locator.payment_menu))
    )