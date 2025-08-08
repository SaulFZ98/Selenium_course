import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


driver=webdriver.Firefox()
t=4

driver.get("https://demoqa.com/")
driver.maximize_window()

title = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
print(title.is_displayed())

bt1 = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")

if(title.is_displayed()==True):
    print("existe la imagen")
    bt1.click()
    time.sleep(t)
else:
    print("no existe la imagen")

time.sleep(t)






driver.close()


