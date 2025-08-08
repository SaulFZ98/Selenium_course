import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(10)

t=1
time.sleep(t)

driver.execute_script("window.scrollTo(0,200)")
nom=driver.find_element(By.XPATH,"//input[contains(@id,'userName')]")
nom.send_keys("saul")
driver.find_element(By.XPATH,"//input[contains(@id,'userEmail')]").send_keys("test@test")
time.sleep(t)
driver.execute_script("window.scrollTo(0,500)")
driver.find_element(By.XPATH,"//button[contains(@id,'submit')]").click()
time.sleep(t)


driver.close()