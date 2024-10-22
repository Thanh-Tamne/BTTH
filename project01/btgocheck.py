from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas
# Đường dẫn đến file thực thi chromedriver
chrome_path = r"D:/python/manguonmo/project1/chromedriver.exe"

# Khởi tạo đối tượng dịch vụ với đường dẫn chromedriver
ser = Service(executable_path=chrome_path)

# Tạo tùy chọn cho Chrome
options = webdriver.ChromeOptions()
options.headless = False  # Tắt chế độ headless để hiện giao diện Chrome nếu muốn

# Khởi tạo driver cho Chrome
driver = webdriver.Chrome(service=ser, options=options)

# Tạo url
url = 'https://gochek.vn/collections/all'

# Truy cập trang web
driver.get(url)


time.sleep(2)


links = driver.find_elements(By.XPATH, "//div[@class='content-product-list product-list filter clearfix']//div[@class='box-pro-detail']/h3/a")

# Lưu tất cả các liên kết sản phẩm
list_links = []
for l in links:
    link = l.get_attribute("href")
    list_links.append(link)

# In ra danh sách liên kết sản phẩm
product =[]
# Lặp qua từng trang chi tiết sản phẩm để lấy thông tin
for link in list_links:
    driver.get(link)
    time.sleep(2)

    # Lấy thông tin sản phẩm
    try:
        tsp = driver.find_element(By.XPATH, "//div[@class='product-title']/h1").text
    except:
        tsp = ""

    try:
        sale = driver.find_element(By.XPATH, "//div[@class='product-price']/span[@class='pro-sale']").text
    except:
        sale = ""

    try:
        price_sale = driver.find_element(By.XPATH, "//div[@class='product-price']/span[@class='pro-price']").text
    except:
        price_sale = ""

    try:
        price_origin = driver.find_element(By.XPATH, "//div[@class='product-price']/del").text
    except:
        price_origin = ""

    product.append({'link sản phẩm': link, 'tên sản phẩm': tsp, 'giá khuyến mãi': price_sale, 'giá gốc': price_origin, 'giảm giá': sale })


product_df = pandas.DataFrame(product)

#lưu thành file excel
a = "product_gocheck.xlsx"
product_df.to_excel(a, index=False)
driver.quit()