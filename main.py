from Asset.startDriver import start_driver
from Asset.userLogin.loginUser import login
from Asset.addtoChart.additemChart import additem


# Inisialisasi driver
driver = start_driver()

# Panggil fungsi login
login(driver)
additem(driver)

# Tunggu beberapa detik lalu tutup browser
driver.quit()