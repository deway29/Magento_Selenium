import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# URL API contoh (gantilah jika menggunakan API lain)
#BASE_URL = "https://reqres.in/api/users"
URL_Createdata = "https://reqres.in/api/users?page=2"
URL_readdata = "https://reqres.in/api/users?page=2"
URL_updatedata  = "https://reqres.in/api/register"
URL_deletedata = "https://reqres.in/api/users/2"

def create_data():
    """Mengirim permintaan POST untuk membuat data baru."""
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(URL_Createdata, json=payload)
    data = response.json()
    
    print("\n[CREATE] Status Code:", response.status_code)
    print("[CREATE] Response:", data)

    assert response.status_code == 201, "Gagal membuat data!"
    return data["id"]  # Mengembalikan ID untuk pengujian selanjutnya

def read_data(post_id):
    """Mengirim permintaan GET untuk membaca data yang dibuat."""
    response = requests.get(f"{URL_readdata}/{post_id}")
    data = response.json()
    
    print("\n[READ] Status Code:", response.status_code)
    print("[READ] Response:", data)

    assert response.status_code == 200, "Gagal membaca data!"
    return data

def update_data(post_id):
    """Mengirim permintaan PUT untuk memperbarui data."""
    payload = {
        "title": "Update API CRUD",
        "body": "Data ini telah diperbarui.",
        "userId": 1
    }
    response = requests.put(f"{URL_updatedata}/{post_id}", json=payload)
    data = response.json()
    
    print("\n[UPDATE] Status Code:", response.status_code)
    print("[UPDATE] Response:", data)

    assert response.status_code == 200, "Gagal memperbarui data!"

def delete_data(post_id):
    """Mengirim permintaan DELETE untuk menghapus data."""
    response = requests.delete(f"{URL_deletedata}/{post_id}")
    
    print("\n[DELETE] Status Code:", response.status_code)
    print("[DELETE] Response:", response.text)

    assert response.status_code == 204, "Gagal menghapus data!"

def test_api_with_selenium():
    """Menguji API yang dipanggil melalui halaman web."""
    options = Options()
    options.add_argument("--headless")  # Jalankan tanpa membuka browser
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://jsonplaceholder.typicode.com/")  # Ganti dengan URL target

    time.sleep(3)  # Tunggu JavaScript memuat data

    try:
        element = driver.find_element(By.TAG_NAME, "pre")
        print("\n[SELENIUM] API Response on Web Page:", element.text)
    except:
        print("\n[SELENIUM] Gagal menemukan elemen yang menampilkan API.")

    driver.quit()

if __name__ == "__main__":
    print("===== Pengujian API CRUD =====")

    # Langkah-langkah CRUD
    post_id = create_data()  # 1. Buat data
    read_data(post_id)       # 2. Baca data
    update_data(post_id)     # 3. Perbarui data
    delete_data(post_id)     # 4. Hapus data

    # Jika ingin menguji API di halaman web
    test_api_with_selenium()
