from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Khởi tạo WebDriver
driver = webdriver.Chrome()

# URL của trang Wikipedia
url = 'https://en.wikipedia.org/wiki/Lists_of_musicians#A'
driver.get(url)
time.sleep(2)

# Tìm và chọn thẻ <ul> thứ 21 chứa danh sách các liên kết
ul_tags = driver.find_elements(By.TAG_NAME, 'ul')
ul_musicians = ul_tags[21]

# Lấy tất cả các thẻ <li> từ <ul> đã chọn
li_tags = ul_musicians.find_elements(By.TAG_NAME, 'li')

# Tạo danh sách để lưu các liên kết
musician_links = []

# Thu thập các đường dẫn từ các thẻ <li>
for li in li_tags:
    try:
        link = li.find_element(By.TAG_NAME, 'a').get_attribute('href')
        musician_links.append(link)
    except:
        continue

# In các đường dẫn đã thu thập
for link in musician_links:
    print(link)

# Lấy danh sách ban nhạc từ trang đầu tiên
driver.get(musician_links[0])
time.sleep(2)

# Tìm thẻ <ul> chứa danh sách ban nhạc và lấy thẻ <li>
ul_tags2 = driver.find_elements(By.TAG_NAME, 'ul')
ul_bands = ul_tags2[24]
li_tags2 = ul_bands.find_elements(By.TAG_NAME, 'li')

# Tạo danh sách để lưu các liên kết ban nhạc
band_links = []

# Thu thập các đường dẫn từ các thẻ <li> trong danh sách ban nhạc
for li in li_tags2:
    try:
        link = li.find_element(By.TAG_NAME, 'a').get_attribute('href')
        band_links.append(link)
    except:
        continue

# Danh sách để lưu dữ liệu các ban nhạc
bands_data = []

# Thu thập thông tin từ từng trang ban nhạc
for link in band_links:
    try:
        driver.get(link)
        time.sleep(2)

        # Trích xuất tên ban nhạc
        try:
            band_name = driver.find_element(By.TAG_NAME, 'h1').text
        except:
            band_name = ""

        # Trích xuất năm hoạt động
        try:
            years_active_element = driver.find_element(By.XPATH, "//th[.//span[text()='Years active']]/following-sibling::td")
            years_active = years_active_element.text
        except:
            years_active = ""

        # Lưu thông tin vào danh sách
        bands_data.append({'name of the band': band_name, 'years active': years_active})

    except Exception as e:
        print(f"Error processing {link}: {e}")

# Tạo DataFrame từ danh sách dữ liệu
bands_df = pd.DataFrame(bands_data)

# Lưu dữ liệu vào file Excel
file_name = "musicians.xlsx"
bands_df.to_excel(file_name, index=False)
print('Đã lưu thành công')

# Đóng trình duyệt
driver.quit()
