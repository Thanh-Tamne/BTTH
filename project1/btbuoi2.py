from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Khởi tạo DataFrame để lưu trữ dữ liệu
d = pd.DataFrame({'name of the band': [], 'years active': []})
musician_data = []
# Khởi động trình duyệt và mở trang Wikipedia
driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Lists_of_musicians#A")
time.sleep(2)

# Lấy tất cả các thẻ (a) với title chứa "List of" và bắt đầu với chữ "A"
tags = driver.find_elements(By.XPATH, "//a[contains(@title,'List of') and starts-with(text(), 'A')]")

# Tạo danh sách các liên kết
links = [tag.get_attribute("href") for tag in tags]

# Kiểm tra và xử lý từng liên kết trong danh sách
for link in links:
    driver.get(link)  # Truy cập vào từng trang nhạc sĩ bắt đầu bằng chữ "A"
    time.sleep(2)  # Chờ trang tải
    

# Lấy tên ban nhạc
#try:
 #   name = driver.find_element(By.TAG_NAME, 'h1').text
#except:
 #   name = " "

# Lấy năm hoạt động
#try:
 #   year_element = driver.find_element(By.XPATH, "//th[.//span[text()='Years active']]/following-sibling::td")
  #  year = year_element.text
#except:
 #   year = " "

# Thêm dữ liệu vào DataFrame
#musician_data.append({'name of the band': name, 'years active': year})
#musician_df = pd.DataFrame(musician_data)
# Xuất ra file Excel
#print("Data exported to musicians.xlsx")

# Đóng trình duyệt
driver.quit()