from Asset.userLogin.loginUser import login
from Asset.startDriver import start_driver


# Inisialisasi driver
driver = start_driver()

# Panggil fungsi login
login(driver)

# Tunggu beberapa detik lalu tutup browser
driver.quit()