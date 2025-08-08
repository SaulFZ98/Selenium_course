import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Firefox()

driver.get("https://syntaxprojects.com/basic-checkbox-demo.php")
driver.maximize_window()
driver.implicitly_wait(10)
t=6

element=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Click on this check box')]")))
element.click()

driver.execute_script("window.scrollTo(0,200)")

element1=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Option 1')]")))
element1.click()

element2=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Option 2')]")))
element2.click()

time.sleep(t)



time.sleep(t)
driver.close()