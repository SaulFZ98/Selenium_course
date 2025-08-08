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

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

boton = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
print(boton.is_enabled())

if(boton.is_enabled()==True):
    print("puedes dar click")
else:
    print("no esta habilitado")
time.sleep(t)






driver.close()


