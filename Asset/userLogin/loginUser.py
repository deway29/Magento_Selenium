from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

def login(driver):
    driver.find_element(By.XPATH, "//div[@class='panel header']//a[contains(.,'Sign In')]").click()
    email_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='base']"))
    )
    email_input = driver.find_element(By.XPATH, "//input[@id='email']")
    email_input.send_keys("JimCarry@icloud.com") 
    time.sleep(2)
    element_hover = driver.find_element(By.XPATH, "//a[contains(.,'Notes')]")
    ActionChains(driver).move_to_element(element_hover).perform()
    time.sleep(2)
    passwordemail_input = driver.find_element(By.XPATH, "//input[@name='login[password]']")
    passwordemail_input.send_keys("@tested123") 
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@class='action login primary']/span[.='Sign In']").click()
    time.sleep(5)
    driver.quit()

