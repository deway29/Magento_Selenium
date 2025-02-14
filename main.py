from Asset.startDriver import start_driver
from Asset.userLogin.loginUser import login
from Asset.addtoChart.additemChart import additem
from Asset.buyProduct.checkOut import checkout

# Inisialisasi driver
driver = start_driver()

# Panggil fungsi login
login(driver)
additem(driver)
checkout(driver)
# Tunggu beberapa detik lalu tutup browser
driver.quit()