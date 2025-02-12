from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Tambahkan import ini
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    # Path ke ChromeDriver (Gunakan raw string r"" atau ganti \ dengan \\)
    driver_path = r"C:\Users\dedew\selenium_python\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    

    # Gunakan Service untuk menginisialisasi WebDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)  # ✅ Ini cara yang benar di Selenium 4

    # Buka Google
    driver.get("https://www.google.com")

    # Tunggu hingga elemen search box muncul
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Masukkan query dan tekan Enter
    search_box.send_keys("Selenium testing automation")
    search_box.send_keys(Keys.RETURN)

    # Tunggu beberapa detik untuk melihat hasil
    time.sleep(5)

except Exception as e:
    print(f"Terjadi error: {e}")

finally:
    # Tutup browser
    driver.quit()
