from selenium import webdriver
from selenium.webdriver.common.by import By
import time # ngưng động thời gian

# khởi tạo Webdriver
driver = webdriver.Chrome()

# mở trang
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22P%22"
driver.get(url)


# đợi khoảng chừng 2 giây
time.sleep(2)

#lấy tất cả các thẻ ul
ul_tags = driver.find_elements(By.TAG_NAME,"ul")
print(len(ul_tags))


#for ul_tag in ul_tags:
#    print(ul_tag.get_attribute())


# chọn thẻ ul thứ 2
ul_painters = ul_tags[20] # list start with index=0

# lấy ra tất cả thẻ <li> thuoc ul_painters
li_tags = ul_painters.find_elements(By.TAG_NAME,"li")

# tao danh sach các url
links = [tag.find_element(By.TAG_NAME,"a").get_attribute("herf")for tag in li_tags]

# tạo danh sách các url
titles = [tag.find_element(By.TAG_NAME,"a").get_attribute("title")for tag in li_tags]

#xuất thông tin
for link in links :
    print(link)
for title in titles:
    print(title)

# đóng web
driver.quit()