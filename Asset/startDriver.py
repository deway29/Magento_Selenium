from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def start_driver():
    # Path ke ChromeDriver (sesuaikan dengan lokasi yang benar)
    webdriver_path = "C:\\Users\\dedew\\selenium_python\\chromedriver-win64\\chromedriver.exe"

    # Gunakan Service() untuk inisialisasi WebDriver
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # Contoh: Buka Google
    driver.get("https://magento.softwaretestingboard.com/")

    return driver