## TC001 Validasi Harga Booking Sesuai Jadwal
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Buka browser
driver = webdriver.Chrome()

# 1. Login sebagai user
driver.get("https://ayo.co.id/")

driver.find_element(By.ID, "sign-in-btn").click()
driver.find_element(By.ID, "_phone").send_keys("test@mail.com")
driver.find_element(By.ID, "btn-check-credential").click()
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "sign-in-btn").click()

# 2. Pilih venue 15
driver.find_element(By.ID, "temukan").click() 
driver.find_element(By.ID, "venue").send_keys("15")

# 3. Pilih tanggal 2022-12-10
driver.find_element(By.ID, "date").send_keys("2022-12-10")

# 4. Pilih jam 09:00 - 11:00
driver.find_element(By.ID, "time-slot").send_keys("09:00-11:00")

# 5. Klik Book
driver.find_element(By.ID, "btn-book").click()

# 6. Simpan booking
driver.find_element(By.ID, "btn-save").click()

time.sleep(2)

# VALIDASI HASIL

# Cek booking berhasil
success_message = driver.find_element(
    By.ID,
    "success-message"
).text

assert success_message == "Booking berhasil dibuat"

# Cek harga yang tampil di UI
price_ui = driver.find_element(
    By.ID,
    "booking-price"
).text

assert price_ui == "1000000"

print("Test Passed")

## TC002 Cegah Double Booking
# =====================
# USER A
# =====================

driver.get("https://ayo.co.id/")

# 1. Login User A
driver.find_element(By.ID, "sign-in-btn").click()
driver.find_element(By.ID, "_phone").send_keys("testA@mail.com")
driver.find_element(By.ID, "btn-check-credential").click()
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "sign-in-btn").click()

# 2. Booking
driver.find_element(By.ID, "venue").send_keys("15")
driver.find_element(By.ID, "date").send_keys("2022-12-10")
driver.find_element(By.ID, "time").send_keys("09:00-11:00")
driver.find_element(By.ID, "btnBook").click()

# 3. Validasi booking berhasil
success = driver.find_element(By.ID, "success-message").text
assert success == "Booking berhasil dibuat"

# Logout
driver.find_element(By.ID, "btnLogout").click()

# =====================
# USER B
# =====================

# 4. Login User B
driver.find_element(By.ID, "sign-in-btn").click()
driver.find_element(By.ID, "_phone").send_keys("testB@mail.com")
driver.find_element(By.ID, "btn-check-credential").click()
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "sign-in-btn").click()

# 5. Booking
driver.find_element(By.ID, "venue").send_keys("15")
driver.find_element(By.ID, "date").send_keys("2022-12-10")
driver.find_element(By.ID, "time").send_keys("09:00-11:00")
driver.find_element(By.ID, "btnBook").click()

# Validasi booking ditolak
error = driver.find_element(By.ID, "error-message").text

assert error == "Selected time is not available"

print("Test Passed")

##TC003 Validasi Slot Bersebelahan
# =====================
# USER A
# =====================

driver.get("https://ayo.co.id/")

# Step 1 - Login User A
driver.find_element(By.ID, "sign-in-btn").click()
driver.find_element(By.ID, "_phone").send_keys("testA@mail.com")
driver.find_element(By.ID, "btn-check-credential").click()
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "sign-in-btn").click()

# Step 2 - Booking Venue 15
driver.find_element(By.ID, "venue").send_keys("15")
driver.find_element(By.ID, "date").send_keys("2022-12-10")
driver.find_element(By.ID, "time").send_keys("09:00-11:00")
driver.find_element(By.ID, "btnBook").click()

# Step 3 - Pastikan Booking Berhasil
success = driver.find_element(By.ID, "success-message").text
assert success == "Booking berhasil dibuat"

# Logout User A
driver.find_element(By.ID, "btnLogout").click()

# =====================
# USER B
# =====================

# Step 4 - Login User B
driver.find_element(By.ID, "sign-in-btn").click()
driver.find_element(By.ID, "_phone").send_keys("testB@mail.com")
driver.find_element(By.ID, "btn-check-credential").click()
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "sign-in-btn").click()

# Step 5 - Booking Slot Berikutnya (11:00-13:00)
driver.find_element(By.ID, "venue").send_keys("15")
driver.find_element(By.ID, "date").send_keys("2022-12-10")
driver.find_element(By.ID, "time").send_keys("11:00-13:00")
driver.find_element(By.ID, "btnBook").click()

# =====================
# VALIDASI
# =====================

# Booking User B berhasil
success = driver.find_element(By.ID, "success-message").text
assert success == "Booking berhasil dibuat"

# Cek data User A tersimpan
userA = driver.find_element(By.ID, "booking-user-1").text
timeA = driver.find_element(By.ID, "booking-time-1").text

assert userA == "User A"
assert timeA == "09:00-11:00"

# Cek data User B tersimpan
userB = driver.find_element(By.ID, "booking-user-2").text
timeB = driver.find_element(By.ID, "booking-time-2").text

assert userB == "User B"
assert timeB == "11:00-13:00"

print("Test Passed")

driver.quit()