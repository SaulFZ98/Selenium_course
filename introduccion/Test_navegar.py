import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#fin by ID
driver=webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(3)

driver.get("https://www.google.com/")
time.sleep(3)

driver.get("https://www.youtube.com/")
time.sleep(3)

driver.execute_script("window.history.go(-1)")
time.sleep(3)

driver.execute_script("window.history.go(-1)")
time.sleep(3)

driver.execute_script("window.history.go(2)")
time.sleep(4)




driver.close()