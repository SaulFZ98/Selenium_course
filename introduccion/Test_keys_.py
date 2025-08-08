import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#fin by ID
driver=webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

driver.execute_script("window.scrollTo(0,200)")
nom=driver.find_element(By.XPATH,"//input[contains(@id,'userName')]")
nom.send_keys("saul")
nom.send_keys(Keys.TAB + "test@test.com" + Keys.TAB + "direccion1" + Keys.TAB + "direcction 2" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(4)



driver.close()