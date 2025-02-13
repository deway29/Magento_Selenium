from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from Asset.userLogin.sourceLogin import resource
import time

locator = resource()

def login(driver):
    driver.find_element(By.XPATH, locator.find_element).click()
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, locator.page))
    )
    email_input = driver.find_element(By.XPATH, locator.email_input)
    email_input.send_keys("JimCarry@icloud.com") 
    time.sleep(2)
    element_hover = driver.find_element(By.XPATH, locator.element_hover)
    ActionChains(driver).move_to_element(element_hover).perform()
    time.sleep(2)
    password_input = driver.find_element(By.XPATH, locator.password_input)
    password_input.send_keys("@tested123") 
    time.sleep(2)
    driver.find_element(By.XPATH, locator.signin).click()
    time.sleep(5)
    

