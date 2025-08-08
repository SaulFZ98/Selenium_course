import time
from selenium.webdriver.common.by import By
from selenium import webdriver
#fin by ID
driver=webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

driver.execute_script("window.scrollTo(0,250)")
nom=driver.find_element(By.ID, "userName")
nom.send_keys("saul")
driver.find_element(By.ID,"userEmail").send_keys("test@test")
time.sleep(1)
driver.execute_script("window.scrollTo(0,500)")
driver.find_element(By.ID,"submit").click()
time.sleep(2)


driver.close()