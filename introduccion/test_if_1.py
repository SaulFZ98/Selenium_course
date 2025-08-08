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

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

title = driver.find_element(By.XPATH, "//h5[contains(.,'Student Registration Form')]")
print(title.is_enabled())
ir = driver.execute_script("arguments[0].scrollIntoView();",title)

if(title.is_enabled()==True):
    print("puedes comenzar a contestar")
    name = driver.find_element(By.XPATH, "//input[contains(@id,'firstName')]").send_keys("saul" + Keys.TAB, "test" + Keys.TAB, "test@test.com")
    gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-1'][contains(.,'Male')]").click()

else:
    print("no esta habilitado")
time.sleep(t)






driver.close()


