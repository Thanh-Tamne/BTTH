from selenium import webdriver
from selenium.webdriver.common.by import By
import time # ngưng động thời gian
import pandas as pd
import re

# tạo dataframe rong
d = pd.DataFrame({'name':[],'birth':[],'death':[],'nationality':[] })

# khởi tạo webdriver
driver = webdriver.Chrome()

# mở trang
url = "https://en.wikipedia.org/wiki/Edvard_Munch"
driver.get(url)

#đợi 2 giây
time.sleep(2)
#lấy tên họa sĩ
try :
    name = driver.find_element(By.TAG_NAME, "h1").text
except:
    name =""
# lấy ngày sinh
try :
    birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
    birth = birth_element.text
    birth = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}',birth)[0]
except:
    birth =""

# lấy ngày mất
try :
    death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
    death = death_element.text
    death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}',death)[0]
except:
    death =""


try :
    nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
    nationality = nationality_element.text

except:
    nationality =""

#tạo dictionary thông tin của họa sĩ
painter= {'name':name,'birth':birth,'death':death,'nationality':nationality}

#chuyển đổi dictionary thành DataFrame
painter_df = pd.DataFrame([painter])

# thêm thông tin vào DF chính
d = pd.concat([d,painter_df],ignore_index=True)

print(d)

# đóng webdriver
driver.quit()