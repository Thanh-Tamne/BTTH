from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

for i in range (65,66) :
    url = "https://en.wikipedia.org/wiki/Lists_of_musicians"
    try :
        driver.get(url)
        time.sleep(2)
        #lay cac the ul
        ul_tags = driver.find_elements(By.TAG_NAME,"ul")
        ul_painters = ul_tags[21]
        li_tags = ul_painters.find_elements(By.TAG_NAME,"li")
        tags = driver.find_elements(By.XPATH, "//a[contains(@title,'List of')]")
        links = [tag.get_attribute("href") for tag in tags]
        for link in links:
            print(link)
    except Exception as e  :
        print("ERROR:" , e)



driver.quit()

