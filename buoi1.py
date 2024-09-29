from selenium import webdriver
from selenium.webdriver.common.by import By
# 2 dong thu vien
import time
# khởi tạo WebDriver
driver = webdriver.Chrome();

#Mở một trang web
driver.get("https://gomotungkinh.com")
time.sleep(5)
# tìm phần tử img có id a=lad "bonk"
bonk_img = driver.find_element(By.ID, "bonk")
# click liên tục vào img "bonk"

while True :
  bonk_img.click()
  print("Clinked on he bonk image")
  time.sleep(0.1)
