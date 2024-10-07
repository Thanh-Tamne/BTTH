from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# đường dẫn đến file thực thi geckodriver
gecko_path = "D:/python/manguonmo/project1/geckodriver.exe"

# khởi tạo đối tượng dịch vụ với đường geckodriver
ser = Service(gecko_path)

# tạo tùy chọn
options = webdriver.firefox.options.Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
#thiết lập firefox chỉ hiển thị giao diện
options.headless = False

#khởi tạo driver
driver = webdriver.Firefox(options = options , service= ser)

#tạo url
url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'

#truy cập
driver.get(url)
# in nội dung cuar trang web
print("Before : ======================")
print(driver.page_source)
# tạm dừng khoảng 3s
time.sleep(3)

# in laij
print("\n\n\n\nafter : ==================\n")
print(driver.page_source )

#dừng lạii
driver.quit()